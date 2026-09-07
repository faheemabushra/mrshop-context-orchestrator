from fastapi import FastAPI
from pydantic import BaseModel

from app.orchestrator.engine import MrShopOrchestrator


app = FastAPI(
    title="Mr.Shop Context Orchestrator",
    description="Prototype conversational AI orchestration system"
)


# Create one orchestrator instance
orchestrator = MrShopOrchestrator()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "Mr.Shop Context Orchestrator is running!"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    result = orchestrator.process_message(
        request.message
    )

    return result