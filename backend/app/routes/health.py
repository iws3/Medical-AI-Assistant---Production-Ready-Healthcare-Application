"""
Health check endpoints
"""

from fastapi import APIRouter
from app.models.schemas import HealthCheckResponse
from datetime import datetime

router = APIRouter(prefix="/api", tags=["Health"])
# when you want to modularize your routes or put them in different files you use APIRouter
# /api/health


@router.get("/health", response_model=HealthCheckResponse)
async def health_check():
    """
    Check if the API is running
    
    Returns:
        Health status
    """
    return HealthCheckResponse(
        status="healthy",
        timestamp=datetime.now(),
        message="MediCare AI Backend is running! 🏥"
    )