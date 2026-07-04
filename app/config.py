from pathlib import Path
from dotenv import load_dotenv
import os

# Корень проекта: .../FreedomAI v1.0.1
ROOT_DIR = Path(__file__).resolve().parents[1]

ENV_PATH = ROOT_DIR / ".env"

print(f"Поиск .env: {ENV_PATH}")

load_dotenv(ENV_PATH)

BOT_TOKEN = os.getenv("BOT_TOKEN")

print(f"BOT_TOKEN найден: {BOT_TOKEN is not None}")

if not BOT_TOKEN:
    raise ValueError(
        f"Файл .env не найден или BOT_TOKEN отсутствует.\n"
        f"Ожидаемый путь: {ENV_PATH}"
    )