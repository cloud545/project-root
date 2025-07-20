
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

def test_analyze_emotion():
    response = client.post("/api/v1/analyze/emotion", json={"text": "I love LangChain!"})
    assert response.status_code == 200
    assert "sentiment" in response.json()
