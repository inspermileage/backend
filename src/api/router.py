from fastapi import APIRouter

from src.api.endpoints import round, track, Telemetry

api_router = APIRouter()
api_router.include_router(round.router, prefix="/round", tags=["Round"])
api_router.include_router(track.router, prefix="/track", tags=["Track"])
api_router.include_router(Telemetry.router, prefix="/telemetry", tags=["Telemetry"])

