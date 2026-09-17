#!/usr/bin/env python3
"""
Bot Message Index Builder for CP3 Demo
Extracts is_bot=True messages from k4_messages.csv and builds a local search index.
This script must be run locally before starting the server; the index is git-ignored.
"""

import csv
import json
import re
from pathlib import Path
from datetime import datetime

# Paths
PACK_CSV = Path(__file__).parent.parent.parent / "data" / "discord-pack" / "k4_messages.csv"
OUTPUT_JSON = Path(__file__).parent / "knowledge" / "bot_messages_index.json"

def sanitize_excerpt(text: str, max_len: int = 200) -> str:
    """
    Sanitize content: mask URLs/passcodes, truncate to max_len.
    """
    if not text:
        return ""
    # Mask URLs that might be invite links or meeting passcodes
    text = re.sub(r'https?://[^\s]+', '[link]', text)
    text = re.sub(r'\b[A-Z0-9]{6,}\b', '[CODE]', text)  # mask passcodes
    # Truncate
    if len(text) > max_len:
        text = text[:max_len] + "…"
    return text.strip()

def extract_facts(content: str, msg_id: str) -> list[str]:
    """
    Extract structured logistics facts from bot message content.
    """
    facts = []
    lower = content.lower()

    # Daily standup
    if "daily" in lower and "standup" in lower:
        if "/daily-standup" in content:
            facts.append("Lệnh báo cáo: /daily-standup")
        if "forum thread" in lower or "thread riêng" in lower:
            facts.append("Nơi gửi: forum thread riêng của nhóm")

    # XP leaderboard
    if "leaderboard" in lower and ("xp" in lower or "điểm" in lower):
        if "/leaderboard users" in content:
            facts.append("Lệnh xem bảng xếp hạng: /leaderboard users")

    # Workshop attendance
    if "workshop" in lower and ("điểm danh" in lower or "attendance" in lower):
        if "email" in lower and "zoom" in lower:
            facts.append("Điều kiện: đăng nhập Zoom bằng email đã đăng ký")
        if "cú pháp" in lower or "tên" in lower:
            facts.append("Điều kiện: đặt tên Zoom đúng cú pháp")
        if "tương tác" in lower:
            facts.append("Điều kiện: tương tác trong buổi workshop")

    # Ticket system
    if "ticket" in lower and ("create" in lower or "tạo" in lower):
        if "/ticket create" in content:
            facts.append("Lệnh tạo ticket hỗ trợ: /ticket create")

    # Lab deadline (generic)
    if "lab" in lower and ("deadline" in lower or "23:59" in content):
        if "23:59" in content:
            facts.append("Hạn nộp Lab: thường là 23:59 cùng ngày")

    # Lab02 - bot explicitly says it does not know
    if "lab02" in lower or "lab 2" in lower:
        if "không có thông tin" in lower or "chưa có thông báo" in lower:
            facts.append("Lab02: bot không có thông tin deadline")

    return facts

def extract_keywords(content: str) -> list[str]:
    """
    Extract search keywords from bot message.
    """
    keywords = set()
    lower = content.lower()

    # Commands
    for cmd in ["/daily-standup", "/leaderboard", "/ticket create", "/myteam"]:
        if cmd in content:
            keywords.add(cmd)

    # Topics
    topic_map = {
        "daily": ["daily", "standup", "báo cáo"],
        "xp": ["xp", "điểm", "leaderboard", "bảng xếp hạng"],
        "workshop": ["workshop", "điểm danh"],
        "ticket": ["ticket", "hỗ trợ"],
        "team": ["team", "nhóm", "đội"],
        "lab": ["lab", "bài tập", "nộp bài"],
        "deadline": ["deadline", "hạn", "23:59"],
        "phoenix": ["phoenix", "api key"],
        "github": ["github", "repo", "commit"],
    }

    for key, terms in topic_map.items():
        if any(t in lower for t in terms):
            keywords.add(key)

    return sorted(keywords)

def build_index():
    """
    Build bot message index from k4_messages.csv where is_bot=True.
    """
    if not PACK_CSV.exists():
        print(f"[!] Pack CSV not found: {PACK_CSV}")
        print("    Place k4_messages.csv in data/discord-pack/ before building the index.")
        return

    print(f"[*] Reading bot messages from {PACK_CSV}")

    bot_messages = []
    with open(PACK_CSV, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            is_bot_val = str(row.get("is_bot", "")).strip().lower()
            if is_bot_val in ("true", "1", "yes"):
                msg_id = row.get("msg_id", "")
                content = row.get("content", "")
                timestamp = row.get("created_at_vn", "")
                channel = row.get("channel", "")

                bot_messages.append({
                    "msg_id": msg_id,
                    "is_bot": True,
                    "timestamp": timestamp,
                    "channel_id": channel,
                    "content_excerpt": sanitize_excerpt(content, max_len=200),
                    "facts": extract_facts(content, msg_id),
                    "keywords": extract_keywords(content),
                })

    print(f"[+] Extracted {len(bot_messages)} bot messages")

    # Write to index
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(bot_messages, f, ensure_ascii=False, indent=2)

    print(f"[+] Index written to {OUTPUT_JSON}")
    print(f"[!] Do NOT commit this file if it contains real pack data.")
    print(f"    Add it to .gitignore: codebase/backend/knowledge/")

if __name__ == "__main__":
    build_index()
