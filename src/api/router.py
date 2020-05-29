from fastapi import APIRouter

from src.api.endpoints import round, track, car, car2

api_router = APIRouter()
api_router.include_router(round.router, prefix="/round", tags=["Round"])
api_router.include_router(track.router, prefix="/track", tags=["Track"])
api_router.include_router(car.router, prefix="/car", tags=["Car"])
api_router.include_router(car2.router, prefix="/car2", tags=["Car2"])
