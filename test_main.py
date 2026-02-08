from datetime import datetime
import yaml

from mailer.send_preview import send_preview_email
from collectors.rss_collector import fetch_rss_items
from collectors.hn_collector import fetch_hn_stories
from ai.summarize_gemini import summarize_items



def load_sources():
    with open("config/sources.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    sources = load_sources()

    # -------- FETCH DATA --------
    rss_items = fetch_rss_items(sources["rss"], limit=6)
    hn_items = fetch_hn_stories(limit=6)

    # -------- GEMINI SUMMARIZATION --------
    top_news_text = summarize_items(rss_items, "Top News")
    signals_text = summarize_items(hn_items, "Signals")

    summary_text = (
        "Key AI updates from official releases and community discussions, "
        "summarized for quick reading."
    )

    # -------- LOAD TEMPLATE --------
    with open("config/template.md", "r", encoding="utf-8") as f:
        template = f.read()

    # -------- FILL TEMPLATE --------
    content = (
        template
        .replace("{{date}}", datetime.now().strftime("%d %b %Y"))
        .replace("{{read_time}}", "5 min")
        .replace("{{summary}}", summary_text)
        .replace("{{top_news}}", top_news_text)
        .replace("{{top_paper}}", "• Coming next (arXiv + Gemini)")
        .replace("{{signals}}", signals_text)
    )

    # -------- SAVE & EMAIL --------
    with open("output/draft_newsletter.md", "w", encoding="utf-8") as f:
        f.write(content)

    send_preview_email(content)


if __name__ == "__main__":
    main()
