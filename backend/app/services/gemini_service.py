"""
Google Gemini AI Service using LangChain
Handles image processing and vision tasks
"""

from langchain_core.messages import HumanMessage
from app.config import load_google_vision_llm
from PIL import Image
import io
import base64


class GeminiService:
    
    
    def __init__(self):
  
        self.vision_llm = load_google_vision_llm()
    
    def extract_text_from_image(self, image_bytes: bytes):
      
        try:
            # Convert image bytes to base64
            image_b64 = base64.b64encode(image_bytes).decode('utf-8')
            
            # Create prompt for text extraction
            extraction_prompt = """You are a medical text extractor. Extract ALL text from this medical document/record.

Include:
- Patient information
- Test results
- Doctor's notes
- Prescriptions
- Dates and measurements
- Any handwritten text

Format the output clearly and preserve the structure. If text is unclear, indicate with [unclear].

Extract all text now:"""
            
            # Create message with image
            message = HumanMessage(
                content=[
                    {"type": "text", "text": extraction_prompt},
                    {
                        "type": "image_url",
                        "image_url": f"data:image/jpeg;base64,{image_b64}"
                    }
                ]
            )
            
            # Invoke the vision model
            response = self.vision_llm.invoke([message])
            
            return response.content
            
        except Exception as e:
            raise Exception(f"Image text extraction error: {str(e)}")
    
    def analyze_image_directly(self, image_bytes: bytes, language: str = "en"):
        """
        Directly analyze medical image and return structured analysis
        
        Args:
            image_bytes: Image file bytes
            language: Response language
            
        Returns:
            Dictionary with analysis
        """
        try:
            # Convert image to base64
            image_b64 = base64.b64encode(image_bytes).decode('utf-8')
            
            # Create analysis prompt
            if language == "fr":
                prompt = """Analysez cette image de dossier médical et fournissez une analyse au format JSON avec ces clés:
- summary: Aperçu bref de ce que vous voyez
- key_findings: Liste des résultats importants
- recommendations: Recommandations de santé
- next_steps: Actions suggérées

Répondez UNIQUEMENT en JSON valide."""
            else:
                prompt = """Analyze this medical record image and provide analysis in JSON format with these keys:
- summary: Brief overview of what you see
- key_findings: List of important findings
- recommendations: Health recommendations
- next_steps: Suggested actions

Respond ONLY with valid JSON."""
            
            # Create message with image
            message = HumanMessage(
                content=[
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": f"data:image/jpeg;base64,{image_b64}"
                    }
                ]
            )
            
            # Invoke vision model
            response = self.vision_llm.invoke([message])
            
            # Parse JSON response
            import json
            result = json.loads(response.content)
            return result
            
        except json.JSONDecodeError:
            return {
                "summary": response.content[:500],
                "key_findings": ["Analysis completed - see summary"],
                "recommendations": ["Consult with a healthcare professional"],
                "next_steps": ["Schedule appointment with your doctor"]
            }
        except Exception as e:
            raise Exception(f"Image analysis error: {str(e)}")


# Global service instance
gemini_service = GeminiService()