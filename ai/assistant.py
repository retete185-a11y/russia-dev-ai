import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("AI_API_KEY")
MODEL = os.getenv("AI_MODEL", "gpt-5.6")

if not API_KEY:
    raise RuntimeError("AI_API_KEY не установлен")

client = OpenAI(api_key=API_KEY)


class RussiaDevAI:

    def __init__(self):
        self.name = "RUSSIA DEV AI"
        self.version = "1.0.0"

    def generate_code(self, request):
        response = client.responses.create(
            model=MODEL,
            instructions=(
                "Ты RUSSIA DEV AI — помощник разработчика RP-проектов. "
                "Помогай создавать оригинальный код, игровые системы, "
                "SQL и структуру проектов. "
                "Не выдавай украденные или закрытые исходники."
            ),
            input=request
        )

        return response.output_text

    def analyze_code(self, code):
        response = client.responses.create(
            model=MODEL,
            instructions=(
                "Ты анализатор кода. "
                "Найди ошибки, объясни причины и предложи исправления."
            ),
            input=code
        )

        return response.output_text
