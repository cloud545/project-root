
from fastapi import APIRouter
from fastapi.openapi.utils import get_openapi

router = APIRouter()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="LangChain Knowledge Base API",
        version="1.0.0",
        description="API for knowledge base management with LangChain integration.",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

# Custom OpenAPI schema
app.openapi = custom_openapi

@router.get("/docs/openapi.json")
async def get_openapi_docs():
    return app.openapi()
