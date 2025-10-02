# Medical AI Assistant - Production-Ready Healthcare Application
<img width="1832" height="845" alt="Screenshot 2025-09-30 061026" src="https://github.com/user-attachments/assets/f09da8d2-626f-4efa-8d12-58ca38ba77e0" />

A production-ready AI-powered medical assistant built with LangChain and Google Gemini 2.0. Demonstrates best practices for building intelligent healthcare applications with natural language processing, document analysis, and research capabilities.



## Demo

[![Demo Preview](https://github.com/user-attachments/assets/f09da8d2-626f-4efa-8d12-58ca38ba77e0)](https://vimeo.com/1123091554)

*Click the preview to watch the full demonstration*



Click the link above to see the Medical AI Assistant in action.
## Features

- **AI Medical Consultation** - Natural language medical Q&A with context-aware responses
- **Medical Record Analysis** - Automated analysis of lab results, prescriptions, and clinical documents
- **OCR Text Extraction** - Extract text from handwritten or printed medical documents
- **Medical Research Search** - Query trusted medical databases (PubMed, WHO, CDC) with AI-powered summarization
- **Bilingual Support** - Complete English and French language support
- **Modern Architecture** - FastAPI, LangChain, Google Gemini 2.0 (free tier available)

## Tech Stack

| Technology | Purpose |
|------------|---------|
| FastAPI | High-performance async backend framework |
| LangChain | AI orchestration and chain operations |
| Google Gemini 2.0 | Multimodal AI model (text + vision) |
| Tavily AI | AI-powered medical research search |
| Pydantic | Data validation and settings management |
| Python 3.11+ | Core programming language |

## Project Structure

```
backend/
├── app/
│   ├── main.py                 # FastAPI application
│   ├── config.py               # Settings & environment
│   ├── routes/
│   │   ├── health.py           # Health check endpoints
│   │   ├── analysis.py         # Medical analysis endpoints
│   │   └── research.py         # Research endpoints
│   ├── services/
│   │   ├── gemini_service.py   # Gemini Vision operations
│   │   └── tavily_service.py   # Medical research
│   ├── chains/
│   │   ├── chat_chain.py       # LangChain chat flows
│   │   └── analysis_chain.py   # LangChain analysis flows
│   └── models/
│       └── schemas.py          # Pydantic data models
├── requirements.txt
├── .env.example
└── README.md
```

## Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- API Keys (both free):
  - [Google Gemini API Key](https://makersuite.google.com/app/apikey)
  - [Tavily API Key](https://tavily.com)

## Quick Start

### 1. Clone and Setup

```bash
git clone https://github.com/yourusername/medical-ai-assistant.git
cd medical-ai-assistant/backend
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Environment

Create a `.env` file in the `backend/` directory:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
HOST=0.0.0.0
PORT=8000
CORS_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
GEMINI_MODEL=gemini-2.0-flash-exp
TEMPERATURE=0.7
MAX_TOKENS=2048
```

**Important:** Add `.env` to `.gitignore` to keep your API keys secure.

### 5. Run the Server

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once running, access the interactive documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Health Check
```
GET /api/health
```
Returns server status and timestamp.

### Medical Chat
```
POST /api/chat
{
  "message": "What are the symptoms of diabetes?",
  "language": "en"
}
```
Get AI-powered medical information in English or French.

### Text Analysis
```
POST /api/analyze-text
{
  "text": "Patient presents with elevated blood pressure...",
  "context": "45-year-old male",
  "language": "en"
}
```
Analyze medical text and receive structured insights.

### Image Analysis
```
POST /api/analyze-image
- file: medical_record.jpg
- language: en
- extract_text_only: false
```
Extract text from medical images and analyze them.

### Text Extraction
```
POST /api/extract-text
- file: prescription.jpg
```
Extract text from medical documents (OCR only).

### Medical Research
```
POST /api/research
{
  "query": "latest treatments for hypertension",
  "max_results": 5,
  "language": "en"
}
```
Search trusted medical databases with AI-generated summaries.

## Testing with Swagger UI

1. Navigate to http://localhost:8000/docs
2. Click on any endpoint to expand it
3. Click "Try it out"
4. Fill in the parameters
5. Click "Execute"
6. View the response below

See the full guide for detailed testing instructions.

## Response Formats

All endpoints return structured JSON with timestamps and proper error handling.

Example chat response:
```json
{
  "response": "Early signs of diabetes include frequent urination...",
  "language": "en",
  "timestamp": "2025-09-30T14:25:30.456789"
}
```

Example analysis response:
```json
{
  "summary": "Blood test shows elevated glucose levels...",
  "key_findings": [
    "Fasting glucose: 126 mg/dL (elevated)",
    "Blood pressure: 150/95 mmHg (stage 1 hypertension)"
  ],
  "recommendations": [
    "Monitor blood sugar levels daily",
    "Reduce sodium intake"
  ],
  "next_steps": [
    "Schedule appointment with endocrinologist",
    "Start dietary modifications"
  ],
  "disclaimer": "This analysis is for informational purposes only...",
  "language": "en",
  "timestamp": "2025-09-30T14:30:15.789012"
}
```

## Architecture Highlights

### LangChain Expression Language (LCEL)
```python
chain = prompt | llm | parser
```
Clean, composable AI workflows with built-in async support and error handling.

### Pydantic Settings Management
Type-safe configuration with automatic validation and IDE autocomplete support.

### Structured Output with PydanticOutputParser
Forces AI models to return valid JSON matching your data models.

### Multimodal AI with Gemini Vision
Processes both text and images in a single model for document analysis.

## Security & Privacy

- Environment variables for sensitive data
- No persistent data storage
- CORS protection enabled
- Input validation with Pydantic
- Medical disclaimer on all responses

## Common Issues

**"Module not found" errors:**
```bash
pip install -r requirements.txt
```

**"Invalid API key" errors:**
- Verify your `.env` file exists
- Check API keys are valid
- Ensure no extra spaces in keys

**Slow responses:**
- Vision/research endpoints take 5-15 seconds (normal)
- Check internet connection
- Monitor API rate limits

## Development

### Running Tests
```bash
pytest
```

### Code Formatting
```bash
black app/
ruff app/
```

### Type Checking
```bash
mypy app/
```

## Deployment

### Docker
```bash
docker build -t medical-ai-assistant .
docker run -p 8000:8000 medical-ai-assistant
```

### Cloud Platforms
- Deploy to Railway, Render, or Google Cloud Run
- Set environment variables in platform settings
- Use production ASGI server (gunicorn + uvicorn)

## Key Learning Points

- **FastAPI** for high-performance async APIs with automatic documentation
- **LangChain LCEL** for composable AI workflows
- **Pydantic** for type-safe data validation and settings
- **Gemini Vision** for multimodal document processing
- **Structured outputs** using PydanticOutputParser
- **Production patterns** for error handling and validation

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

MIT License - see LICENSE file for details

## Acknowledgments

- Built with [LangChain](https://python.langchain.com/)
- Powered by [Google Gemini 2.0](https://ai.google.dev/)
- Search by [Tavily AI](https://tavily.com/)
- Framework by [FastAPI](https://fastapi.tiangolo.com/)

## Support

- Open an issue for bugs or feature requests
- Check the [full documentation](https://dev.to/fonyuygita/building-a-production-ready-medical-ai-assistant-with-python-fastapi-tavili-gemini-langchain-5693) for detailed guides
- Join discussions in the Issues tab

## Disclaimer

This application is for educational and demonstration purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of qualified health providers with questions about medical conditions.

---

**Building Production-Ready AI Applications with Modern Python Stack**
