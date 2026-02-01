import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"

def summarize_text(text: str) -> str:
    payload = {
        "model": MODEL,
        "prompt": f"""
        Summarize the following text in 5 clear bullet points.
        Be concise and professional.

        TEXT:
        {text}
        """,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    return response.json()["response"]


if __name__ == "__main__":
    sample_text = """
    Artificial intelligence is transforming industries by automating tasks,
    improving decision-making, and enabling new products and services.
    """

    summary = summarize_text(sample_text)
    print(summary)
