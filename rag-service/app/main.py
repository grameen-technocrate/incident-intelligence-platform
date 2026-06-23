from fastapi import FastAPI

app = FastAPI(
    title="Incident Intelligence Platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "application": "Incident Intelligence Platform",
        "service": "RAG API",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
@app.get("/mintoo")
def mintoo():
    return {
        "Name": "Hey! Its Mintoo"
    }