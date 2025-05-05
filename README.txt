This application retrieves news articles on specific topics from "newsapi.org", and creates personalized summaries based on user preferences.
-----------------------------------------------------------------
Features:

1- Search for news on specific topics: Find articles and generate summaries.
2- Save topics of interest: Save your topics.
3- View customized summaries: Get summaries for your saved topics.
4- See search history: Keep your previous searches.
-----------------------------------------------------------------
Requirements

-Python 3.8+
-NewsAPI key (https://newsapi.org/)
-Groq API key (https://groq.com/)
-Required Python packages: "newsapi", "sentence-transformers", "faiss", "langchain", "python-dotenv"
-----------------------------------------------------------------
Create a ".env" file and add your API keys:

-NEWSAPI_KEY= newsapi_key
-GROQ_API_KEY= groq_api_key
-----------------------------------------------------------------
Run the application from terminal:

"python main.py"
-----------------------------------------------------------------
1- news_retriever.py: Find news articles from NewsAPI.

2- embedding_engine.py: Embeddings for articles using "all-MiniLM-L6-v2" model.

3- summarizer.py: Summaries using "llama3-8b-8192" model.

4- user_manager.py: Manages user preferences, search history, and embeddings.

5- main.py: Main application interface.
-----------------------------------------------------------------
Usage:

1- Search for news on specific topics:
	Enter a topic (e.g., "Artificial Intelligence").


2- Save topics of interest:
	Enter a topic to save (e.g., "Healthcare").
	The topic will be added to your preferences.

3- View customized summaries: 
	View summaries form your saved topics.

4- See search history: 
	View your search history.

5- Exit the application.
-----------------------------------------------------------------
Troubleshooting

-Check your NewsAPI key and ensure it’s valid.
-Check if there is articles found or NOT.
-Ensure the Groq API key is valid and the model is accessible.