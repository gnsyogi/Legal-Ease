from fastapi import FastAPI
from backend.routes import router

app = FastAPI(title="LegalEase API")

@app.get("/")
def home():
    return {"message": "LegalEase Backend Running"}

app.include_router(router)
