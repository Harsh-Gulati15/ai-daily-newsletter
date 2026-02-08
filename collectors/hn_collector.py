import requests

HN_TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
HN_ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

def fetch_hn_stories(limit=5):
    story_ids = requests.get(HN_TOP_STORIES_URL).json()
    stories = []

    for story_id in story_ids[:limit]:
        item = requests.get(HN_ITEM_URL.format(story_id)).json()
        if item and item.get("type") == "story":
            stories.append({
                "title": item.get("title"),
                "score": item.get("score", 0),
                "comments": item.get("descendants", 0),
                "url": item.get("url", ""),
                "source": "Hacker News"
            })

    return stories
