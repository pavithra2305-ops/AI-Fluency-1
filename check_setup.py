import os
from dotenv import load_dotenv

load_dotenv()

provider = os.getenv("PROVIDER")
model = os.getenv("MODEL")

if provider and model:
    print("SETUP OK")
    print(f"Provider: {provider}")
    print(f"Model: {model}")
else:
    print("SETUP ERROR")