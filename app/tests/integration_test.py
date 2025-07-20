
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_create_knowledge_base():
    response = client.post("/api/v1/knowledge/base/create", json={
        "company_id": 2001,
        "name": "Test Knowledge Base",
        "description": "Test description",
        "type": "text"
    })
    assert response.status_code == 200
    assert "knowledge_base_id" in response.json()

def test_upload_document():
    file_content = "This is a test document content."
    response = client.post("/api/v1/document/upload", json={
        "kb_id": 1,
        "company_id": 2001,
        "file": file_content
    })
    assert response.status_code == 200
    assert "file_path" in response.json()

def test_analyze_emotion():
    response = client.post("/api/v1/analyze/emotion", json={"text": "I love LangChain!"})
    assert response.status_code == 200
    assert "sentiment" in response.json()

def test_memory_save_and_get():
    content = "Test memory content"
    doc_id = 1
    response_save = client.post("/api/v1/memory/save", json={"doc_id": doc_id, "content": content})
    assert response_save.status_code == 200

    response_get = client.get(f"/api/v1/memory/get/{doc_id}")
    assert response_get.status_code == 200
    assert "memory" in response_get.json()
