from fastapi import FastAPI
from api.voice import router as voice_router
app=FastAPI(
    title="Jaspa",
    description="Jarvis Jr. A Voice Operating System",
    version="1.0"
)
app.include_router(voice_router)
@app.get("/")
def root():
    return {
        "status":"online",
        "project":"Jaspa"
    }
@app.get("/health")
def health():
    return {
        "healthy":True
    }