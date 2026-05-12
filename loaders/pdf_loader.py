from langchain_community.document_loaders import PyPDFLoader

def load_pdf(pdf_path):
    
    try:
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()
        print(f"Successfully loaded PDF: {pdf_path}")
        print(f"Total pages loaded: {len(documents)}")
        return documents
    except Exception as e:
        print(f"Error loading PDF: {e}")
        return []
    