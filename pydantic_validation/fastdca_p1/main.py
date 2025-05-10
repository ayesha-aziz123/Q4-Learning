from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from uuid import uuid4
from typing import List, Dict

# 🌐 Initialize FastAPI App
app = FastAPI(title="Simple Chatbot API")

# 🧠 In-Memory Database (stores chat history for each user)
chat_db: Dict[str, List[dict]] = {}

# ---------------------------
# 🧾 Data Models
# ---------------------------

# Model for chat config metadata
class ChatConfig(BaseModel):
    model: str
    temperature: float = 0.7
    top_p: float = 0.9

# Model for individual messages
class ChatMessage(BaseModel):
    role: str  # "user" or "bot"
    content: str

# Model for chat request body
class ChatRequest(BaseModel):
    user_id: str
    config: ChatConfig
    messages: List[ChatMessage]

# Metadata in chat response
class ChatReplyMetadata(BaseModel):
    timestamp: str
    session_id: str

# Model for chat response
class ChatReply(BaseModel):
    user_id: str
    reply: str
    metadata: ChatReplyMetadata

# ---------------------------
# 🚀 POST /chat — Handle chat request
# ---------------------------

@app.post("/chat", response_model=ChatReply)
def handle_chat(request: ChatRequest):
    if not request.messages:
        raise HTTPException(status_code=400, detail="Message list cannot be empty")

    last_msg = request.messages[-1].content.strip()
    if not last_msg:
        raise HTTPException(status_code=400, detail="Last message content is empty")

    # Store user message in chat_db
    user_history = chat_db.setdefault(request.user_id, [])
    user_history.append({
        "role": "user",
        "content": last_msg,
        "timestamp": datetime.utcnow().isoformat()
    })

    # Dummy bot reply
    bot_reply = "Hello, how are you batman?"

    # Store bot response
    user_history.append({
        "role": "bot",
        "content": bot_reply,
        "timestamp": datetime.utcnow().isoformat()
    })

    return ChatReply(
        user_id=request.user_id,
        reply=bot_reply,
        metadata=ChatReplyMetadata(
            timestamp=datetime.utcnow().isoformat(),
            session_id=str(uuid4())
        )
    )
# ---------------------------
# 📜 GET /history/{user_id} — User's full chat history
# ---------------------------

@app.get("/history/{user_id}")
def get_user_history(user_id: str):
    if user_id not in chat_db:
        raise HTTPException(status_code=404, detail="User ID not found")

    return {
        "user_id": user_id,
        "history": chat_db[user_id]
    }

# ---------------------------
# 👥 GET /users — List all user IDs
# ---------------------------

@app.get("/users")
def list_all_users():
    return {
        "users": list(chat_db.keys())
    }
