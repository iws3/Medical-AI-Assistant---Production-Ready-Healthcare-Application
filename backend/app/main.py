"""
MediCare AI - FastAPI Main Application
Entry point for the backend server with LangChain integration
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routes import health, analysis, research

# Create FastAPI app
app = FastAPI(
    title="MediCare AI Backend",
    description="Medical AI Assistant API for Cameroon 🏥 - Powered by LangChain",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router)
app.include_router(analysis.router)
app.include_router(research.router)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to MediCare AI Backend 🏥",
        "version": "2.0.0",
        "powered_by": "LangChain + Google Gemini",
        "docs": "/docs",
        "status": "running"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=True
    )