# import os

# from dotenv import load_dotenv

# load_dotenv()

from langchain_huggingface import HuggingFaceEmbeddings

#from langchain_google_genai import GoogleGenerativeAIEmbeddings

def get_embedding_model():
    """Initialize and return the embedding model."""
    try:
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        return embeddings
    except Exception as e:
        print(f"Error initializing embedding model: {e}")
        return None
