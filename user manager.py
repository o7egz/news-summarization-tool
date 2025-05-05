import json
import os
from embedding_engine import EmbeddingEngine

class UserManager:
    def __init__(self, user_id):
        self.user_id = user_id
        self.preferences_file = "user_preferences.json"
        self.preferences = self._load_preferences()
        self.embedding_engine = EmbeddingEngine() # initialize Embedding Engine

    def _load_preferences(self):
        if os.path.exists(self.preferences_file):
            with open(self.preferences_file, "r") as f:
                user_data = json.load(f)
                return user_data.get(self.user_id, {})
        return {}

    def save_preferences(self, preferences):
        user_data = {}
        if os.path.exists(self.preferences_file):
            with open(self.preferences_file, "r") as f:
                user_data = json.load(f)
        user_data[self.user_id] = preferences
        with open(self.preferences_file, "w") as f:
            json.dump(user_data, f)

    def add_topic(self, topic):
        if "topics" not in self.preferences:
            self.preferences["topics"] = []
        if topic not in self.preferences["topics"]:
            self.preferences["topics"].append(topic)
            self.save_preferences(self.preferences)

    def get_topics(self):
        return self.preferences.get("topics", [])

    def add_search_history(self, query):
        if "search_history" not in self.preferences:
            self.preferences["search_history"] = []
        self.preferences["search_history"].append(query)
        self.save_preferences(self.preferences)

    def get_search_history(self):
        return self.preferences.get("search_history", [])

    def create_embeddings_for_articles(self, articles):
        self.embedding_engine.create_embeddings(articles)

    def search_similar_articles(self, query, k=3):
        return self.embedding_engine.search_similar(query, k)