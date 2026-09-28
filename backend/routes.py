from fastapi import APIRouter
from backend.models import DocumentRequest
from backend.ai_core.gemini_generator import GeminiDocumentGenerator

router = APIRouter()

@router.post("/generate")
def generate_doc(request: DocumentRequest):
    result = GeminiDocumentGenerator.generate_document(request)
    return {"document": result}
