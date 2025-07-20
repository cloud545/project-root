
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base

class KnowledgeBase(Base):
    __tablename__ = "knowledge_base"
    
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, index=True)
    name = Column(String(255), index=True)
    type = Column(String(50))
    description = Column(Text)
    created_at = Column(String(255))  # Store timestamp as string (for simplicity)

    documents = relationship("KnowledgeDocument", back_populates="knowledge_base")

class KnowledgeDocument(Base):
    __tablename__ = "knowledge_document"
    
    id = Column(Integer, primary_key=True, index=True)
    kb_id = Column(Integer, ForeignKey("knowledge_base.id"))
    company_id = Column(Integer)
    filename = Column(String(255))
    file_path = Column(String(255))
    status = Column(String(50))
    created_at = Column(String(255))  # Store timestamp as string (for simplicity)
    
    knowledge_base = relationship("KnowledgeBase", back_populates="documents")
