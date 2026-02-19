from fastapi import FastAPI
from app.routers import resume, ai

app = FastAPI(title = "AI Career Backend")

app.include_router(resume.router, prefix='/resume', tags=["Resume"])
app.include_router(ai.router, prefix='/ai', tags=["AI"])

@app.get("/health")
def health_check():
    return {"status": "Backend is running"}
