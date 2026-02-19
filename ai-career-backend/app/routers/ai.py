from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai_service import get_career_suggestions

router = APIRouter()

class SuggestionRequest(BaseModel):
    skills: list[str]

@router.post("/suggestions")
def suggestions(request: SuggestionRequest):
    return {
    "career_suggestions": get_career_suggestions(request.skills)
}
