import feedparser

def fetch_rss_items(feed_urls, limit=5):
    items = []

    for url in feed_urls:
        feed = feedparser.parse(url)
        for entry in feed.entries[:limit]:
            items.append({
                "title": entry.title,
                "summary": entry.get("summary", ""),
                "link": entry.link,
                "source": feed.feed.get("title", "RSS")
            })

    return items
