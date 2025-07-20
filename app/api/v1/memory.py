
from fastapi import APIRouter, HTTPException
from app.services.chroma import collection

router = APIRouter()

@router.post("/memory/save")
async def save_memory(doc_id: int, content: str):
    try:
        # Store memory in Chroma
        vector = embed_document(content)  # assuming the embed_document function is available
        collection.add({"id": str(doc_id), "vector": vector})
        return {"status": "success", "doc_id": doc_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/memory/get/{doc_id}")
async def get_memory(doc_id: int):
    try:
        # Fetch memory from Chroma
        memory = collection.get([str(doc_id)])
        return {"doc_id": doc_id, "memory": memory}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)}
