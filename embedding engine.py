import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
load_dotenv() # Load API key from .env file

class EmbeddingEngine:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')  
        self.dimension = self.model.get_sentence_embedding_dimension()  
        self.index = None  
        self.articles = []  
    def create_embeddings(self, articles):
        contents = [article["content"] for article in articles if article["content"]] # Extract article content

        embeddings = self.model.encode(contents, show_progress_bar=True)
        self.index = faiss.IndexFlatL2(self.dimension) # FAISS index for storing embeddings
        self.index.add(np.array(embeddings).astype('float32'))  # Add embeddings to the index
        self.articles = articles # Store article

    def search_similar(self, query, k=5):
        if not self.index:
            raise ValueError("FAISS index not initialized. Call create_embeddings first.")

        query_embedding = self.model.encode([query])
        query_embedding = np.array(query_embedding).astype('float32')
        distances, indices = self.index.search(query_embedding, k) # for similar articles
        similar_articles = []
        for idx in indices[0]:
            if idx != -1: # FAISS returns -1 for invalid indices
                similar_articles.append(self.articles[idx])
        return similar_articles