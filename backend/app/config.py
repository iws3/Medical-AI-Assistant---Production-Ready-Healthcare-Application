"""
Configuration management for MediCare AI
Loads environment variables and LangChain models
"""

import os
from functools import lru_cache
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load variables from .env file into environment
load_dotenv()


class Settings:
    """Application settings loaded from environment variables"""

    # API Keys
    google_api_key: str = os.getenv("GOOGLE_API_KEY")
    tavily_api_key: str = os.getenv("TAVILY_API_KEY", "DUMMY_TAVILY_KEY")

    # Server settings
    host: str = os.getenv("HOST", "0.0.0.0")
    port: int = int(os.getenv("PORT", 8000))
    cors_origins: str = os.getenv("CORS_ORIGINS", "http://localhost:3000")

    # AI Model settings
    gemini_model: str = os.getenv("GEMINI_MODEL", "gemini-2.0-flash-exp")
    temperature: float = float(os.getenv("TEMPERATURE", 0.7))
    max_tokens: int = int(os.getenv("MAX_TOKENS", 2048))

    # File upload settings
    max_file_size: int = int(os.getenv("MAX_FILE_SIZE", 10 * 1024 * 1024))  # 10MB

    @property
    def cors_origins_list(self):
        """Convert comma-separated CORS origins to list"""
        return [origin.strip() for origin in self.cors_origins.split(",")]


# Global settings instance
settings = Settings()
print(f"google  api key is: {settings.google_api_key} and port is {settings.port}")


@lru_cache()
def load_google_llm():
    """
    Load Google Gemini LLM with LangChain
    Cached to avoid recreating on every request
    """
    return ChatGoogleGenerativeAI(
        model=settings.gemini_model,
        google_api_key=settings.google_api_key,
        temperature=settings.temperature,
        max_output_tokens=settings.max_tokens,
        convert_system_message_to_human=True,  # Gemini compatibility
    )


@lru_cache()
def load_google_vision_llm():
    """
    Load Google Gemini with vision capabilities
    """
    return ChatGoogleGenerativeAI(
        model=settings.gemini_model,
        google_api_key=settings.google_api_key,
        temperature=0.5,  # Lower temp for consistent extraction
        max_output_tokens=settings.max_tokens,
        convert_system_message_to_human=True,
    )
