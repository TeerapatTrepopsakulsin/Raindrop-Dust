import time
import struct
import asyncio
from machine import Pin, I2C, ADC, UART
from dht import DHT11
import network
import json
from umqtt.robust import MQTTClient
from config import (
   WIFI_SSID, WIFI_PASS,
   MQTT_BROKER, MQTT_USER, MQTT_PASS
)




class UartError(Exception):
   pass




class Pms7003:


   START_BYTE_1 = 0x42
   START_BYTE_2 = 0x4d


   PMS_FRAME_LENGTH = 0
   PMS_PM1_0 = 1
   PMS_PM2_5 = 2
   PMS_PM10_0 = 3
   PMS_PM1_0_ATM = 4
   PMS_PM2_5_ATM = 5
   PMS_PM10_0_ATM = 6
   PMS_PCNT_0_3 = 7
   PMS_PCNT_0_5 = 8
   PMS_PCNT_1_0 = 9
   PMS_PCNT_2_5 = 10
   PMS_PCNT_5_0 = 11
   PMS_PCNT_10_0 = 12
   PMS_VERSION = 13
   PMS_ERROR = 14
   PMS_CHECKSUM = 15


   def __init__(self, uart):
       self.uart = UART(uart, baudrate=9600, tx=Pin(19), rx=Pin(18), timeout=100)


   def __repr__(self):
       return "Pms7003({})".format(self.uart)


   @staticmethod
   def _assert_byte(byte, expected):
       if byte is None or len(byte) < 1 or ord(byte) != expected:
           return False
       return True


   @staticmethod
   def _format_bytearray(buffer):
       return "".join("0x{:02x} ".format(i) for i in buffer)


   def _send_cmd(self, request, response):


       nr_of_written_bytes = self.uart.write(request)


       if nr_of_written_bytes != len(request):
           raise UartError('Failed to write to UART')


       if response:
           time.sleep(2)
           buffer = self.uart.read(len(response))


           if buffer != response:
               raise UartError(
                   'Wrong UART response, expecting: {}, getting: {}'.format(
                       Pms7003._format_bytearray(response), Pms7003._format_bytearray(buffer)
                   )
               )




   def read(self):


       while True:


           first_byte = self.uart.read(1)
           if not self._assert_byte(first_byte, Pms7003.START_BYTE_1):
               continue


           second_byte = self.uart.read(1)
           if not self._assert_byte(second_byte, Pms7003.START_BYTE_2):
               continue


           # we are reading 30 bytes left
           read_bytes = self.uart.read(30)
           if len(read_bytes) < 30:
               continue


           data = struct.unpack('!HHHHHHHHHHHHHBBH', read_bytes)


           checksum = Pms7003.START_BYTE_1 + Pms7003.START_BYTE_2
           checksum += sum(read_bytes[:28])


           if checksum != data[Pms7003.PMS_CHECKSUM]:
               continue


           return {
               'frame_length': data[Pms7003.PMS_FRAME_LENGTH],
               'pm1_0': data[Pms7003.PMS_PM1_0],
               'pm2_5': data[Pms7003.PMS_PM2_5],
               'pm10_0': data[Pms7003.PMS_PM10_0],
               'pm1_0_atm': data[Pms7003.PMS_PM1_0_ATM],
               'pm2_5_atm': data[Pms7003.PMS_PM2_5_ATM],
               'pm10_0_atm': data[Pms7003.PMS_PM10_0_ATM],
               'pcnt_0_3': data[Pms7003.PMS_PCNT_0_3],
               'pcnt_0_5': data[Pms7003.PMS_PCNT_0_5],
               'pcnt_1_0': data[Pms7003.PMS_PCNT_1_0],
               'pcnt_2_5': data[Pms7003.PMS_PCNT_2_5],
               'pcnt_5_0': data[Pms7003.PMS_PCNT_5_0],
               'pcnt_10_0': data[Pms7003.PMS_PCNT_10_0],
               'version': data[Pms7003.PMS_VERSION],
               'error': data[Pms7003.PMS_ERROR],
               'checksum': data[Pms7003.PMS_CHECKSUM],
           }




class AQI:
   AQI = (
       (0, 50),
       (51, 100),
       (101, 150),
       (151, 200),
       (201, 300),
       (301, 400),
       (401, 500),
   )


   _PM2_5 = (
       (0, 12),
       (12.1, 35.4),
       (35.5, 55.4),
       (55.5, 150.4),
       (150.5, 250.4),
       (250.5, 350.4),
       (350.5, 500.4),
   )


   _PM10_0 = (
       (0, 54),
       (55, 154),
       (155, 254),
       (255, 354),
       (355, 424),
       (425, 504),
       (505, 604),
   )


   @classmethod
   def PM2_5(cls, data):
       return cls._calculate_aqi(cls._PM2_5, data)


   @classmethod
   def PM10_0(cls, data):
       return cls._calculate_aqi(cls._PM10_0, data)


   @classmethod
   def _calculate_aqi(cls, breakpoints, data):
       for index, data_range in enumerate(breakpoints):
           if data <= data_range[1]:
               break


       i_low, i_high = cls.AQI[index]
       C_low, c_high = data_range
       return (i_high - i_low) / (c_high - C_low) * (data - C_low) + i_low


   @classmethod
   def aqi(cls, pm2_5_atm, pm10_0_atm):
       pm2_5 = cls.PM2_5(pm2_5_atm)
       pm10_0 = cls.PM10_0(pm10_0_atm)
       return max(pm2_5, pm10_0)




class KidBright:
   __instance = None


   SECOND = 1000
   MINUTE = 60 * SECOND


   def __new__(cls):
       if cls.__instance is None:
           cls.__instance = super(KidBright, cls).__new__(cls)
           cls.__instance.__init__()
       return cls.__instance


   def __init__(self):
       self.__topic = None


       # LED
       self.green = Pin(12, Pin.OUT)
       self.red = Pin(2, Pin.OUT)


       self.resting()


       # Temp sensors
       # Set I2C channel 1 to Pin #4 and #5
       self.i2c = I2C(1, sda=Pin(4), scl=Pin(5))
       # Specify the register address to measure the current temperature
       self.i2c.writeto(77, bytearray([0]))


       # Light sensors
       self.ldr = ADC(Pin(36))


       # Humidity sensors
       self.hum = DHT11(Pin(32))


       # Dust sensors
       self.pms = Pms7003(2)


       # WI-FI
       self.wlan = network.WLAN(network.STA_IF)


       # MQTT
       self.mqtt = MQTTClient(client_id="",
                              server=MQTT_BROKER,
                              user=MQTT_USER,
                              password=MQTT_PASS)


       self.state = self.publishing




   def read_temperature(self):
       data = self.i2c.readfrom(77, 2)
       value = (256 * data[0] + data[1]) / 128
       return value


   def read_light_percentage(self):
       return 100 - (self.ldr.read() / 4095 * 100)


   def read_light(self):
       light_data = self.ldr.read_uv() / 1e6  # read light data in volt
       r = (light_data * 33000 / (3.3 - light_data)) / 1e3  # calculate r ldr in kOhm
       lux = 1e4 / pow(r * 10, 4 / 3)
       return lux


   def read_humidity(self):
       while True:
           try:
               self.hum.measure()
               humidity = self.hum.humidity()
               return humidity
           except OSError:
               print("Failed to read sensor.")
           time.sleep_ms(100)


   def read_dust(self) -> dict[str, float|int]:
       return self.pms.read()


   @staticmethod
   def aqi(dust_data: dict[str, float|int]):
       return AQI.aqi(dust_data['pm2_5_atm'], dust_data['pm10_0_atm'])


   async def connect(self):
       """Connect WI-FI and MQTT"""
       self.wlan.active(True)
       self.wlan.connect(WIFI_SSID, WIFI_PASS)
       while not self.wlan.isconnected():
           await asyncio.sleep_ms(int(0.5 * KidBright.SECOND))
       self.mqtt.connect()


   def publishing(self):
       self.green.value(0)
       self.red.value(1)


   def resting(self):
       self.green.value(1)
       self.red.value(0)


   def toggle_led(self):
       self.state()


   async def publish_into_db(self):
       while True:
           # green when publishing
           self.publishing()


           await self.connect()


           # Read weather data
           temp = self.read_temperature()
           light = self.read_light()
           hum = self.read_humidity()
           pms_data = self.read_dust()
           aqi = self.aqi(pms_data)
           lat = 13.84474491
           lon = 100.56421035
           data = {
               'light': light,
               'temp': temp,
               'hum': hum,
               'aqi': aqi,
           }
           data.update(pms_data)


           print("publishing...", data)


           await self.publish(data)
           await asyncio.sleep_ms(KidBright.SECOND)
           await self.disconnect()


           # red when not publishing
           self.resting()


           await asyncio.sleep_ms(10 * KidBright.MINUTE)


   async def publish(self, data):
       """Publish data to MQTT topic"""
       self.mqtt.publish(self.topic, json.dumps(data))
       await asyncio.sleep_ms(0)


   async def disconnect(self):
       """Disconnect WI-FI and MQTT"""
       self.mqtt.disconnect()
       self.wlan.disconnect()
       await asyncio.sleep_ms(0)


   @property
   def topic(self) -> str:
       return self.__topic


   @topic.setter
   def topic(self, topic):
       self.__topic = topic




MQTT_TOPIC = "b6610545324/raindropdust"




async def main():
   kb = KidBright()
   kb.topic = MQTT_TOPIC
   await kb.publish_into_db()




asyncio.create_task(main())
asyncio.run_until_complete()
