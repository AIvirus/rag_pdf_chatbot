import os
from dotenv import load_dotenv

load_dotenv()

print("Loaded HF Token:", os.getenv("HUGGINGFACEHUB_API_TOKEN"))
print("GEMINI KEY:", os.getenv("GEMINI_API_KEY"))
print("OPENAI API", os.getenv("OPENAI_API_KEY"))

