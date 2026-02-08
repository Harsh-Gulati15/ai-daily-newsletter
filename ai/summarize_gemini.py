from google import genai
import os

API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise RuntimeError(
        "GOOGLE_API_KEY not set. Run: setx GOOGLE_API_KEY <your_key> and reopen terminal."
    )

client = genai.Client(api_key=API_KEY)


def summarize_items(items, category):
    if not items:
        return "No significant updates today."

    headlines = "\n".join([f"- {item['title']}" for item in items])

    prompt = f"""
You are writing a daily AI industry newsletter.

Category: {category}

Headlines:
{headlines}

For the most important items:
- Write a short headline
- What happened (1–2 lines)
- Why it matters (1 line)

Style rules:
- Clear, factual, concise
- No hype, no emojis
- Plain text only
"""

    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    )

    return response.text.strip()
