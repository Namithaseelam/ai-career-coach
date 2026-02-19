from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai_service import generate_resume


router = APIRouter()


class ResumeRequest(BaseModel):
    name: str
    skills: list[str]
    experience: str

@router.post('/generate')
def create_resume(request: ResumeRequest):
    return {
        "generated_resume": generate_resume(request)
    }
