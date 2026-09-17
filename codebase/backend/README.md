# Backend — CP3 Discord Assistant Demo

FastAPI server with OpenRouter tool calling for the CP3 logistics assistant.

## Setup

1. **Install dependencies:**
   ```bash
   cd codebase/backend
   pip install -r requirements.txt
   ```

2. **Set your OpenRouter API key locally:**
   ```bash
   cp .env.example .env
   # Edit .env and add your OPENROUTER_API_KEY
   ```

3. **Build the bot-message index:**
   ```bash
   python build_index.py
   ```
   
   This reads `../../data/discord-pack/k4_messages.csv` and creates `knowledge/bot_messages_index.json`.
   
   **⚠️ Do NOT commit the index if built from the real CSV.** It's git-ignored by default.

4. **Start the server:**
   
   From the repository root:
   ```bash
   uvicorn codebase.backend.app:app --reload --port 8000
   ```
   
   The backend loads `codebase/backend/.env` automatically when present.

5. **Check health:**
   ```
   GET http://127.0.0.1:8000/api/health
   ```
   Should return `api_configured: true` and `bot_index_present: true`.

## API Contract

### POST /api/ask

Request:
```json
{
  "question": "Lệnh báo cáo daily standup là gì?"
}
```

Response:
```json
{
  "answer": "Lệnh báo cáo daily standup là /daily-standup, gửi trong forum thread riêng của nhóm.",
  "state": "VERIFIED_OFFICIAL",
  "confidence": "high",
  "citations": [
    {
      "msg_id": "M96777",
      "excerpt": "**Daily Standup** là hoạt động báo cáo tiến độ...",
      "timestamp": "2026-09-12 11:30",
      "trust": "BOT_OFFICIAL"
    }
  ],
  "trace": {
    "tool_called": true,
    "tool_name": "search_bot_messages",
    "result_count": 1
  }
}
```

**States:**
- `VERIFIED_OFFICIAL`: answer backed by a bot-authored (`is_bot=True`) record from the pack
- `CLARIFY`: question missing an identifier (which Lab, which form)
- `NOT_FOUND`: no bot record supports the fact
- `REFUSE`: request is outside authority (approve absence, reopen form, grade)
- `REDIRECT_ACADEMIC`: academic/explanatory question belongs in VLearn Tutor

## Data Safety

- The server **never** serves the raw CSV or human-authored messages.
- Only short, sanitized bot excerpts and structured facts are returned.
- Invite URLs and passcodes are masked in the index builder.
- The local trace (`traces/agent_trace.jsonl`) records query, tool name, source IDs, state, and latency—it does not log model reasoning or user-identifiable data.

## Authority Predicate

A record is authoritative **exactly when** `is_bot=True` in the Discord pack. Human-authored announcements, TA responses, and student questions are excluded by design. The 313 bot messages are concentrated in `channel_10` and are replies to student questions, not standalone announcements.

This narrow filter is a CP3 team decision; future iterations may refine the source registry.
