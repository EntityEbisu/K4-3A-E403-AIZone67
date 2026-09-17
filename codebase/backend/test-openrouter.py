import os
from openai import OpenAI
from dotenv import load_dotenv

# 1. Load .env file
load_dotenv()

# 2. Get credentials
api_key = os.getenv("OPENROUTER_API_KEY")
model_id = os.getenv("OPENROUTER_MODEL", "google/gemma-4-26b-a4b-it:free") # Default example

if not api_key:
    print("❌ Error: OPENROUTER_API_KEY not found in .env")
    exit()

# 3. Initialize Client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

try:
    print(f"🚀 Testing OpenRouter model: {model_id}...")
    
    # 4. Make a simple completion request
    response = client.chat.completions.create(
        model=model_id,
        messages=[
            {"role": "user", "content": "Say 'OpenRouter is live' if you can read this."}
        ],
        max_tokens=10
    )

    # 5. Check result
    content = response.choices[0].message.content
    print("✅ Success! API Key is live and model is responsive.")
    print(f"🤖 Response: {content}")

except Exception as e:
    print(f"❌ Failed: {e}")