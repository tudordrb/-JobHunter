import json
import requests

from app.models import Job
from app.ai.prompts import SYSTEM_PROMPT


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen3:8b"


def analyze_job(job: Job) -> int:
    prompt = f"""
{SYSTEM_PROMPT}

JOB TITLE:
{job.title}

JOB DESCRIPTION:
{job.description}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
            "format": "json",
            "options": {
                "temperature": 0
            }
        },
        timeout=120,
    )

    response.raise_for_status()

    try:
        response_json = response.json()
    except Exception as e:
        raise RuntimeError(
            f"Nu am putut citi răspunsul Ollama.\n\n{e}"
        )

    if "response" not in response_json:
        raise RuntimeError(
            f"Răspuns invalid de la Ollama:\n\n{response_json}"
        )

    raw = response_json["response"].strip()

    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        raise RuntimeError(
            f"Ollama nu a returnat JSON valid:\n\n{raw}"
        )

    if "score" not in data:
        raise RuntimeError(
            f"Lipsește cheia 'score'.\n\n{data}"
        )

    score = int(data["score"])

    if score < 0:
        score = 0

    if score > 100:
        score = 100

    return score