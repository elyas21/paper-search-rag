import numpy as np
from langchain_community.llms import ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

class PaperSummarizer:
    def __init__(self):
        self.llm = ollama.Ollama(
            model="llama3.2:1b",
            callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
        )

    def summarize_paper(self, title, abstract, details):
        """Summarize the paper using LLM."""
        paper_text = f"Title: {title}\nAbstract: {abstract}\n"
        if details:
            paper_text += f"Authors: {', '.join(details.get('authors', []))}\nJournal: {details.get('journal', 'N/A')}\nPublished: {details.get('publication_date', 'N/A')}"
        summary = self.llm(f"Summarize the following paper: {paper_text}")
        return summary

    def embed_paper(self, title, abstract, details):
        """Generate a vector embedding for the paper."""
        # For now, we will return a random vector as a placeholder
        # Replace this with an actual embedding model in production
        return np.random.rand(512).tolist()  # Example of a 512-dimensional vector
