"""
LangChain chains for medical record analysis
Uses structured output with Pydantic models
"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from app.config import load_google_llm
from app.models.schemas import MedicalAnalysis


def create_analysis_chain(language: str = "en"):
    """
    Create a chain for structured medical record analysis
    
    How it works:
    1. User provides medical record text
    2. Prompt instructs LLM to analyze in structured format
    3. LLM generates JSON response
    4. Parser converts JSON to Pydantic model
    
    Args:
        language: Response language (en/fr)
        
    Returns:
        Runnable chain that outputs MedicalAnalysis
    """
    # Load the LLM
    llm = load_google_llm()
    
    # Create Pydantic parser - forces structured output
    parser = PydanticOutputParser(pydantic_object=MedicalAnalysis)
    
    # Get format instructions from parser
    format_instructions = parser.get_format_instructions()
    
    # Create prompt based on language
    if language == "fr":
        system_message = """Vous êtes un assistant médical IA analysant des dossiers médicaux.
Fournissez des informations claires, précises et actionnables.
Restez objectif et recommandez toujours une consultation médicale professionnelle."""
        
        user_template = """Analysez ce dossier médical et fournissez une analyse structurée:

Dossier Médical:
{medical_text}

Contexte Additionnel:
{context}

{format_instructions}

Répondez UNIQUEMENT en JSON valide."""
    else:
        system_message = """You are a medical AI assistant analyzing medical records.
Provide clear, accurate, and actionable insights.
Stay objective and always recommend professional medical consultation."""
        
        user_template = """Analyze this medical record and provide a structured analysis:

Medical Record:
{medical_text}

Additional Context:
{context}

{format_instructions}

Respond ONLY with valid JSON."""
    
    # Create the chat prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_message),
        ("user", user_template)
    ])
    
    # Partially fill in format instructions
    prompt = prompt.partial(format_instructions=format_instructions)
    
    # Chain: prompt → llm → parser
    chain = prompt | llm | parser
    
    return chain


def analyze_medical_record(text: str, context: str = "", language: str = "en"):
    """
    Analyze medical record text and return structured results
    
    Args:
        text: Medical record text
        context: Additional patient context
        language: Response language
        
    Returns:
        MedicalAnalysis object with structured data
    """
    # Create the chain
    chain = create_analysis_chain(language)
    
    # Invoke the chain
    try:
        result = chain.invoke({
            "medical_text": text,
            "context": context if context else "No additional context provided"
        })
        return result
    except Exception as e:
        # Fallback if parsing fails
        print(f"Analysis error: {e}")
        return MedicalAnalysis(
            summary=f"Analysis completed but encountered formatting issues: {str(e)[:200]}",
            key_findings=["Analysis was performed but results need manual review"],
            recommendations=["Consult with a healthcare professional for detailed interpretation"],
            next_steps=["Schedule appointment with your doctor", "Keep this record for your medical history"]
        )


# Example usage (for testing):
# if __name__ == "__main__":
#     test_text = """
#     Patient: John Doe
#     Blood Pressure: 140/90 mmHg
#     Blood Sugar: 180 mg/dL (fasting)
#     Diagnosis: Hypertension, Pre-diabetes
#     """
#     result = analyze_medical_record(test_text)
#     print(result.summary)
#     print(result.key_findings)