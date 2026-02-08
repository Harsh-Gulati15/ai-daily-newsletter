from datetime import datetime
import yaml

from mailer.send_preview import send_preview_email
from collectors.rss_collector import fetch_rss_items
from collectors.hn_collector import fetch_hn_stories


def load_sources():
    with open("config/sources.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    sources = load_sources()

    # -------- TOP NEWS (RSS) --------
    rss_items = fetch_rss_items(sources["rss"], limit=5)

    if rss_items:
        top_news = "\n".join([f"• {item['title']}" for item in rss_items])
        summary = "Auto-generated from AI company blog updates and community signals."
    else:
        top_news = "• No major official updates today."
        summary = "Quiet day for official AI announcements."

    # -------- SIGNALS (HACKER NEWS) --------
    hn_items = fetch_hn_stories(limit=5)

    if hn_items:
        signals = "\n".join([
            f"• {item['title']} (HN ↑{item['score']})"
            for item in hn_items
        ])
    else:
        signals = "• No major Hacker News discussions today."

    # -------- LOAD TEMPLATE --------
    with open("config/template.md", "r", encoding="utf-8") as f:
        template = f.read()

    # -------- FILL TEMPLATE --------
    content = (
        template
        .replace("{{date}}", datetime.now().strftime("%d %b %Y"))
        .replace("{{read_time}}", "4 min")
        .replace("{{summary}}", summary)
        .replace("{{top_news}}", top_news)
        .replace("{{top_paper}}", "• Coming next (Gemini-powered paper summary)")
        .replace("{{signals}}", signals)
    )

    # -------- SAVE & EMAIL --------
    with open("output/draft_newsletter.md", "w", encoding="utf-8") as f:
        f.write(content)

    send_preview_email(content)


if __name__ == "__main__":
    main()
