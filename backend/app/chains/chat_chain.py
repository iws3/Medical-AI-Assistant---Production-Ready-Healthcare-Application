"""
LangChain chains for chat functionality
Simple, beginner-friendly implementation
"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.config import load_google_llm


def create_chat_chain(language: str = "en"):
    

    # Load the LLM
    llm = load_google_llm()
    
    # Create prompt template based on language
    if language == "fr":
        system_message = """Vous êtes MediCare AI, un assistant médical IA pour le Cameroun.

Vos responsabilités:
- Fournir des informations médicales précises et basées sur des preuves
- Expliquer les concepts médicaux en termes simples
- Toujours recommander de consulter un professionnel de santé qualifié
- Être culturellement sensible au contexte camerounais

IMPORTANT: Vous n'êtes PAS un médecin. Ne donnez jamais de diagnostic définitif."""
    else:
        system_message = """You are MediCare AI, a medical AI assistant for Cameroon.

Your responsibilities:
- Provide accurate, evidence-based medical information
- Explain medical concepts in simple terms
- Always recommend consulting qualified healthcare professionals
- Be culturally sensitive to the Cameroonian context

IMPORTANT: You are NOT a doctor. Never provide definitive diagnoses."""
    
    # Create the chat prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_message),
        ("user", "{user_question}")
    ])
    
    # Create output parser
    parser = StrOutputParser()
    
    # Chain them together using LCEL (LangChain Expression Language)
    # This is like: prompt → llm → parser
    chain = prompt | llm | parser
    
    return chain


def get_chat_response(message: str, language: str = "en"):
   
    # Create the chain
    chain = create_chat_chain(language)
    
    # Invoke the chain with user's message
    response = chain.invoke({
        "user_question": message
    })
    
    return response


# Example usage (for testing):
# if __name__ == "__main__":
#     response = get_chat_response("What are symptoms of malaria?", "en")
#     print(response)