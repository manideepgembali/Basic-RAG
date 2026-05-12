import os

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


# Load environment variables
load_dotenv()


def get_llm():
    """
    Creates Gemini LLM
    """

    try:

        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0,
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )

        print("LLM initialized successfully")

        return llm

    except Exception as e:
        print(f"Error initializing LLM: {e}")
        return None


def format_docs(docs):
    """
    Combines retrieved documents
    """

    return "\n\n".join(doc.page_content for doc in docs)


def create_rag_chain(retriever, prompt, llm):
    """
    Creates LCEL RAG chain
    """

    try:

        rag_chain = (
            {
                "context": retriever | format_docs,
                "question": RunnablePassthrough(),
            }
            | prompt
            | llm
            | StrOutputParser()
        )

        print("LCEL RAG chain created successfully")

        return rag_chain

    except Exception as e:
        print(f"Error creating RAG chain: {e}")
        return None