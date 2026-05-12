from langchain_community.vectorstores import FAISS

def create_vector_store(documents,embedding_model):
    """Create and return a FAISS vector store."""
    try:
        vector_store = FAISS.from_documents(documents, embedding_model)
        print("FAISS vector store created successfully")
        return vector_store
    except Exception as e:
        print(f"Error creating vector store: {e}")
        return None

