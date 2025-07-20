
@router.post("/knowledge/base/create")
async def create_knowledge_base(company_id: int, name: str, description: str, type: str):
    db = SessionLocal()
    try:
        kb = KnowledgeBase(company_id=company_id, name=name, description=description, type=type, created_at="2023-09-01")
        db.add(kb)
        db.commit()
        return {"status": "success", "knowledge_base_id": kb.id}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()

@router.get("/knowledge/base/{kb_id}")
async def get_knowledge_base(kb_id: int):
    db = SessionLocal()
    try:
        kb = db.query(KnowledgeBase).filter(KnowledgeBase.id == kb_id).first()
        if not kb:
            raise HTTPException(status_code=404, detail="Knowledge Base not found")
        return {"knowledge_base": kb}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()
