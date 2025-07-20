
from fastapi import APIRouter, HTTPException
from transformers import pipeline

router = APIRouter()

# Load the sentiment analysis model from HuggingFace
sentiment_analyzer = pipeline("sentiment-analysis")

@router.post("/analyze/emotion")
async def analyze_emotion(text: str):
    try:
        result = sentiment_analyzer(text)
        sentiment = result[0]["label"]
        score = result[0]["score"]
        return {"sentiment": sentiment, "score": score}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
