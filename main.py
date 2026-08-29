from fastapi import FastAPI
from pydantic import BaseModel

from ai.assistant import RussiaDevAI

app = FastAPI(
    title="RUSSIA DEV AI",
    description="AI-помощник для разработки RP-проектов",
    version="1.0.0"
)

ai = RussiaDevAI()


class CodeRequest(BaseModel):
    request: str


class AnalyzeRequest(BaseModel):
    code: str


@app.get("/")
def home():
    return {
        "name": "RUSSIA DEV AI",
        "version": "1.0.0",
        "status": "online"
    }


@app.post("/generate")
def generate_code(data: CodeRequest):
    result = ai.generate_code(data.request)

    return {
        "success": True,
        "result": result
    }


@app.post("/analyze")
def analyze_code(data: AnalyzeRequest):
    result = ai.analyze_code(data.code)

    return {
        "success": True,
        "result": result
    }
