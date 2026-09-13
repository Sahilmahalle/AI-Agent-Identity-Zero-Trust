from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="AI Agent Identity & Zero Trust API",
    description="Foundation API for the AI Agent Identity and Zero Trust project",
    version="0.1.0",
)


class EchoRequest(BaseModel):
    message: str


@app.get("/health")
def health_check():
    """
    Basic service health check.
    """
    return {
        "status": "ok",
        "service": "ai-agent-zero-trust-api",
    }


@app.get("/agent")
def agent_info():
    """
    Temporary agent information endpoint.
    This endpoint will be protected by identity and policy controls
    in later milestones.
    """
    return {
        "agent_id": "soc-analyst-agent",
        "agent_type": "security-analysis",
        "status": "active",
        "trust_level": "unverified",
    }


@app.post("/echo")
def echo_message(request: EchoRequest):
    """
    Simple POST endpoint used to demonstrate JSON request handling.
    """
    return {
        "received": request.message,
        "length": len(request.message),
    }