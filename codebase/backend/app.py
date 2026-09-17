"""FastAPI entrypoint for the local CP3 Discord assistant demo."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from .agent import ask_gemini
from .tools import INDEX_PATH

# Load environment from .env if present (OPENROUTER_API_KEY, OPENROUTER_MODEL)
load_dotenv(Path(__file__).parent / ".env", override=False)

ROOT = Path(__file__).parent.parent
FRONTEND_DIR = ROOT / "frontend"

app = FastAPI(title="CP3 Discord Assistant", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000", "http://localhost:8000"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


class AskRequest(BaseModel):
    question: str = Field(min_length=1, max_length=1000)


@app.get("/api/health")
def health() -> dict[str, Any]:
    return {
        "ok": True,
        "provider": "openrouter",
        "model": os.getenv("OPENROUTER_MODEL", "openai/gpt-4-turbo"),
        "api_configured": bool(os.getenv("OPENROUTER_API_KEY")),
        "bot_index_present": INDEX_PATH.exists(),
    }


@app.post("/api/ask")
def ask(request: AskRequest) -> dict[str, Any]:
    question = request.question.strip()
    if not question:
        raise HTTPException(status_code=422, detail="question must not be empty")
    return ask_gemini(question)


if FRONTEND_DIR.exists():
    app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")
