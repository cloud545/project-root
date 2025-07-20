
from fastapi import APIRouter, HTTPException
from app.services.qa import ask_question

router = APIRouter()

@router.post("/query")
async def query_knowledge(question: str, role_system_prompt: str = "You are a helpful assistant."):
    try:
        answer = ask_question(role_system_prompt, question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
