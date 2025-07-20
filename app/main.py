from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.db import init_db
from app.api.v1.router import router as api_router  # Correct import statement

app = FastAPI(
    title="LangChain Knowledge Base API",
    description="Knowledge base management system with LangChain integration.",
    version="1.0.0",
)

# Initialize the database
init_db()

# Include API router
app.include_router(api_router, prefix="/api/v1", tags=["api"])

@app.get("/health", tags=["health"])
async def health_check():
    return JSONResponse(content={"status": "healthy"})
