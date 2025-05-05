import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate
from langchain.docstore.document import Document
load_dotenv() # Load API key from .env file

class Summarizer:
    def __init__(self, temperature=0.7):
        GROQ_API_KEY = os.getenv("GROQ_API_KEY")  
        self.model = ChatGroq(
            temperature=temperature,
            model_name="llama3-8b-8192",  
            groq_api_key=GROQ_API_KEY
        )

    def brief_summary(self, articles):
        contents = [article["content"] for article in articles if article.get("content")]
        docs = [Document(page_content=content) for content in contents]
        # prompt for brief summarization
        prompt_template = """
                Write a concise summary (1-2 sentences) of the following articles. Focus on the main topic and the most important details of each article. Avoid minor details or examples.

                Article:
                {text}

                Summary:
                """

        prompt = PromptTemplate(template=prompt_template, input_variables=["text"])
        chain = load_summarize_chain(self.model, chain_type="map_reduce", map_prompt=prompt, combine_prompt=prompt) # Create map_reduce chain
        result = chain.invoke({"input_documents": docs})
        return result["output_text"]

    def detailed_summary(self, articles):
        contents = [article["content"] for article in articles if article.get("content")]
        docs = [Document(page_content=content) for content in contents]
        # prompt for detailed summarization
        prompt_template = """
            Write a detailed summary (1 paragraph) of the following articles. Cover the main topic, key points, and any significant details of each article. Be specific and avoid generic statements.

            Article:
            {text}

            Summary:
            """

        prompt = PromptTemplate(template=prompt_template, input_variables=["text"])
        chain = load_summarize_chain(self.model, chain_type="refine", question_prompt=prompt, refine_prompt=prompt)
        result = chain.invoke({"input_documents": docs})
        return result["output_text"]