def create_retriever(vector_store):
    """Create and return a retriever from the given vector store."""
    try:
        retriever = vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 3}
        )
        print("Retriever created successfully")
        return retriever
    except Exception as e:
        print(f"Error creating retriever: {e}")
        return None