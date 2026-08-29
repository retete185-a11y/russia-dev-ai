from fastapi import FastAPI

app = FastAPI(
    title="RUSSIA DEV AI",
    description="AI-помощник для разработки RP-проектов",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "name": "RUSSIA DEV AI",
        "version": "1.0.0",
        "status": "online"
    }

@app.get("/about")
def about():
    return {
        "features": [
            "Генерация кода",
            "Создание игровых систем",
            "Анализ кода",
            "Генерация файлов проекта"
        ]
    }
