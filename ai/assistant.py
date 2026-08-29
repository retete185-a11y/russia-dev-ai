import os

from dotenv import load_dotenv
from openai import OpenAI

from ai.prompts import SYSTEM_PROMPT, GENERATOR_PROMPT

load_dotenv()

API_KEY = os.getenv("AI_API_KEY")
MODEL = os.getenv("AI_MODEL")

if not API_KEY:
    raise RuntimeError("AI_API_KEY не установлен")

if not MODEL:
    raise RuntimeError("AI_MODEL не установлен")

client = OpenAI(api_key=API_KEY)


class RussiaDevAI:

    def __init__(self):
        self.name = "RUSSIA DEV AI"
        self.version = "1.0.0"

    def generate_code(self, request: str):
        prompt = GENERATOR_PROMPT.format(request=request)

        response = client.responses.create(
            model=MODEL,
            instructions=SYSTEM_PROMPT,
            input=prompt
        )

        return response.output_text

    def analyze_code(self, code: str):
        response = client.responses.create(
            model=MODEL,
            instructions=SYSTEM_PROMPT,
            input=(
                "Проанализируй следующий код. "
                "Найди ошибки и предложи исправления:\n\n"
                + code
            )
        )

        return response.output_text
