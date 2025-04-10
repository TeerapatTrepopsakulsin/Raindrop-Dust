from fastapi import APIRouter


router = APIRouter(
    prefix="/forecast",
    tags=["forecast"],
    responses={
        404: {"description": "Not found"}
    }
)


@router.post("/")
async def forecast():
    # TODO: Implement forecasting logic
    return {"forecast": "result"}
