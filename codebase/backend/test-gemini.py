import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Load environment variables from .env file
load_dotenv()

# 2. Get credentials from .env
api_key = os.getenv("GEMINI_API_KEY")
model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite") # Default to flash if not set

if not api_key:
    print("❌ Error: GEMINI_API_KEY not found in .env file")
    exit()

# 3. Configure the API
genai.configure(api_key=api_key)

try:
    # 4. Select the model
    model = genai.GenerativeModel(model_name)
    
    # 5. Send a test prompt
    print(f"🚀 Testing model: {model_name}...")
    response = model.generate_content("Say 'Hello World' if you can read this.")
    
    # 6. Check response
    if response.text:
        print("✅ Success! API Key is live and model is usable.")
        print(f"🤖 Response: {response.text}")
    else:
        print("⚠️ Response received but empty.")

except Exception as e:
    print(f"❌ Failed: {e}")