"""
Medical record analysis endpoints using LangChain
"""

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.models.schemas import (
    ChatRequest, ChatResponse,
    AnalysisRequest, AnalysisResponse,
    ImageAnalysisResponse
)
from app.chains.chat_chain import get_chat_response
from app.chains.analysis_chain import analyze_medical_record
from app.services.gemini_service import gemini_service
from datetime import datetime

router = APIRouter(prefix="/api", tags=["Analysis"])


@router.post("/chat", response_model=ChatResponse)
async def chat_with_ai(request: ChatRequest):
    """
    Chat with AI about medical questions
    Uses LangChain chat chain for responses
    
    Args:
        request: Chat request with message and language
        
    Returns:
        AI response
    """
    try:
        # Use LangChain chat chain
        response_text = get_chat_response(
            message=request.message,
            language=request.language
        )
        
        return ChatResponse(
            response=response_text,
            language=request.language,
            timestamp=datetime.now()
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chat error: {str(e)}")


@router.post("/analyze-text", response_model=AnalysisResponse)
async def analyze_medical_text(request: AnalysisRequest):
    """
    Analyze medical record text
    Uses LangChain analysis chain with structured output
    
    Args:
        request: Analysis request with text and optional context
        
    Returns:
        Structured analysis
    """
    try:
        # Use LangChain analysis chain
        analysis = analyze_medical_record(
            text=request.text,
            context=request.context,
            language=request.language
        )
        
        disclaimer = (
            "⚠️ This analysis is for informational purposes only. "
            "Always consult qualified healthcare professionals for medical advice."
        )
        
        return AnalysisResponse(
            summary=analysis.summary,
            key_findings=analysis.key_findings,
            recommendations=analysis.recommendations,
            next_steps=analysis.next_steps,
            disclaimer=disclaimer,
            language=request.language,
            timestamp=datetime.now()
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis error: {str(e)}")


@router.post("/analyze-image", response_model=ImageAnalysisResponse)
async def analyze_medical_image(
    file: UploadFile = File(...),
    language: str = Form(default="en"),
    extract_text_only: bool = Form(default=False)
):
    """
    Analyze medical record image (lab results, hospital book, etc.)
    Uses Gemini Vision for text extraction
    Uses LangChain for analysis
    
    Args:
        file: Image file upload
        language: Response language (en/fr)
        extract_text_only: If True, only extract text without analysis
        
    Returns:
        Extracted text and analysis
    """
    # Validate file type
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    try:
        # Read image bytes
        image_bytes = await file.read()
        
        # Extract text from image using Gemini Vision
        extracted_text = gemini_service.extract_text_from_image(image_bytes)
        
        if extract_text_only:
            # Return only extracted text
            return ImageAnalysisResponse(
                extracted_text=extracted_text,
                analysis=AnalysisResponse(
                    summary="Text extraction completed",
                    key_findings=[],
                    recommendations=[],
                    next_steps=["Review the extracted text", "Analyze if needed"],
                    disclaimer="Text extraction only - no analysis performed",
                    language=language,
                    timestamp=datetime.now()
                )
            )
        
        # Perform full analysis using LangChain
        analysis = analyze_medical_record(
            text=extracted_text,
            language=language
        )
        
        disclaimer = (
            "⚠️ This analysis is for informational purposes only. "
            "Always consult qualified healthcare professionals for medical advice."
        )
        
        return ImageAnalysisResponse(
            extracted_text=extracted_text,
            analysis=AnalysisResponse(
                summary=analysis.summary,
                key_findings=analysis.key_findings,
                recommendations=analysis.recommendations,
                next_steps=analysis.next_steps,
                disclaimer=disclaimer,
                language=language,
                timestamp=datetime.now()
            )
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image analysis error: {str(e)}")


@router.post("/extract-text")
async def extract_text_from_image(file: UploadFile = File(...)):
    """
    Extract text from medical record image (OCR only)
    
    Args:
        file: Image file upload
        
    Returns:
        Extracted text
    """
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    try:
        image_bytes = await file.read()
        extracted_text = gemini_service.extract_text_from_image(image_bytes)
        
        return {
            "extracted_text": extracted_text,
            "timestamp": datetime.now()
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Text extraction error: {str(e)}")