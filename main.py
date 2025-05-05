from dotenv import load_dotenv
from news_retriever import NewsRetriever
from summarizer import Summarizer
from user_manager import UserManager
load_dotenv() # Load API key from .env file

def main():
    news_retriever = NewsRetriever()
    summarizer = Summarizer()
    user_id = "user"  
    user_manager = UserManager(user_id)

    while True:
        print("\nNews Summarization Tool")
        print("1. Search for news on specific topics")
        print("2. Save topics of interest")
        print("3. View customized summaries")
        print("4. See search history")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            query = input("Enter topic search: ")
            articles = news_retriever.get_articles(query, page_size=3)
            if not articles:
                print("No articles found.")
                continue
            user_manager.create_embeddings_for_articles(articles)
            brief_summary = summarizer.brief_summary(articles)
            detailed_summary = summarizer.detailed_summary(articles)
            print(f"\nBrief Summary for '{query}':")
            print(brief_summary)
            print(f"\nDetailed Summary for '{query}':")
            print(detailed_summary)
            user_manager.add_search_history(query)

        elif choice == "2":
            topic = input("Enter topic to save: ")
            user_manager.add_topic(topic)
            print(f"Topic '{topic}' saved.")

        elif choice == "3":
            topics = user_manager.get_topics()
            if not topics:
                print("No topics saved.")
                continue
            for topic in topics:
                print(f"\nFetching articles for topic: {topic}")
                articles = news_retriever.get_articles(topic, page_size=3)
                if not articles:
                    print(f"No articles found for topic '{topic}'.")
                    continue
                user_manager.create_embeddings_for_articles(articles)
                brief_summary = summarizer.brief_summary(articles)
                detailed_summary = summarizer.detailed_summary(articles)
                print(f"\nBrief Summary for '{topic}':")
                print(brief_summary)
                print(f"\nDetailed Summary for '{topic}':")
                print(detailed_summary)

        elif choice == "4":
            search_history = user_manager.get_search_history()
            if not search_history:
                print("No history found.")
            else:
                print("\nSearch History:")
                for query in search_history:
                    print(f"- {query}")

        elif choice == "5":
            print("bye.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()