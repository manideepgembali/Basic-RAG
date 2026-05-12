from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(documents):
    try:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        return text_splitter.split_documents(documents)
    except Exception as e:
        print(f"Error splitting documents: {e}")
        return []