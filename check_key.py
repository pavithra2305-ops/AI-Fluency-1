from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("GROQ_API_KEY")

if key:
    print("Groq API key found")
    print("Starts with:", key[:4])
    print("Key length:", len(key))
else:
    print("Groq API key NOT found")