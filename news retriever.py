import os
from newsapi import NewsApiClient
from dotenv import load_dotenv
load_dotenv() # Load API key from .env file

class NewsRetriever:
    def __init__(self):
        self.newsapi = NewsApiClient(api_key=os.getenv("NEWSAPI_KEY"))

    def get_articles(self, query, language="en", page_size=3):
        try:
            response = self.newsapi.get_everything(
                q=query, # Search
                language=language,  
                page_size=page_size, # Number of articles
                sort_by="relevancy"  
            )

            articles = []
            for article in response["articles"]:
                articles.append({
                    "title": article["title"],
                    "description": article["description"],
                    "content": article["content"],
                    "url": article["url"]
                })

            return articles

        except Exception as e:
            print(f"Error fetching articles: {e}")
            return []