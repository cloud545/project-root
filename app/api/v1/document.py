
from fastapi import APIRouter, File, UploadFile, HTTPException
from app.models import KnowledgeBase, KnowledgeDocument
from app.db import SessionLocal
from app.utils.cache import set_to_cache

router = APIRouter()

@router.post("/document/upload")
async def upload_document(kb_id: int, company_id: int, file: UploadFile = File(...)):
    db = SessionLocal()
    try:
        kb = db.query(KnowledgeBase).filter(KnowledgeBase.id == kb_id, KnowledgeBase.company_id == company_id).first()
        if not kb:
            raise HTTPException(status_code=404, detail="Knowledge Base not found")

        # Store file to disk
        file_path = f"storage/knowledge/{company_id}/{kb_id}/{file.filename}"
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        # Insert document record into DB
        doc = KnowledgeDocument(kb_id=kb_id, company_id=company_id, filename=file.filename, file_path=file_path, status="uploaded", created_at="2023-09-01")
        db.add(doc)
        db.commit()

        # Optionally store document info in Redis cache for quick access
        set_to_cache(f"document:{doc.id}", file_path)

        return {"status": "success", "file_path": file_path, "document_id": doc.id}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()
