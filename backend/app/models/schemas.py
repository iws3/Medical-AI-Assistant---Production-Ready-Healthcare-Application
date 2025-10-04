"""
Pydantic models for request/response validation
"""

from pydantic import BaseModel, Field
from datetime import datetime


class HealthCheckResponse(BaseModel):
    """Health check endpoint response"""
    status: str
    timestamp: datetime
    message: str


class ChatRequest(BaseModel):
    
    message: str = Field(..., min_length=1, max_length=1000, description="User's medical question")
    language: str = Field(default="en", description="Response language (en/fr)")


class ChatResponse(BaseModel):
   
    response: str
    language: str
    timestamp: datetime


class AnalysisRequest(BaseModel):
    """Medical record analysis request (for text input)"""
    text: str = Field(..., min_length=1, description="Medical record text to analyze")
    context: str = Field(default="", description="Additional context about the patient")
    language: str = Field(default="en", description="Response language")


class MedicalAnalysis(BaseModel):
   
    summary: str = Field(description="Brief overview of the medical record")
    key_findings: list[str] = Field(description="List of important findings")
    recommendations: list[str] = Field(description="Health recommendations")
    next_steps: list[str] = Field(description="Suggested next steps")


class AnalysisResponse(BaseModel):
    
    summary: str
    key_findings: list[str]
    recommendations: list[str]
    next_steps: list[str]
    disclaimer: str
    language: str
    timestamp: datetime


class ImageAnalysisResponse(BaseModel):
    """Image analysis response"""
    extracted_text: str
    analysis: AnalysisResponse


class ResearchRequest(BaseModel):
    """Research request model"""
    query: str = Field(..., min_length=3, max_length=200, description="Medical topic to research")
    max_results: int = Field(default=5, ge=1, le=10, description="Number of results")
    language: str = Field(default="en", description="Response language")


class ResearchResult(BaseModel):
    """Single research result"""
    title: str
    url: str
    content: str
    score: float


class ResearchResponse(BaseModel):
    """Research response model"""
    query: str
    results: list[ResearchResult]
    summary: str
    timestamp: datetime