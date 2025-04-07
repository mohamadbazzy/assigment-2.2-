# app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .model import SentimentAnalyzer

app = FastAPI(title="Sentiment Analysis API")
model = SentimentAnalyzer()

class TextRequest(BaseModel):
    text: str

@app.post("/analyze")
def analyze_sentiment(request: TextRequest):
    try:
        result = model.analyze(request.text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"message": "Welcome to the Sentiment Analysis API"}