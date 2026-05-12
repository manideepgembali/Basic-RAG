# Basic-RAG

A simple Retrieval-Augmented Generation (RAG) system built with LangChain, FAISS, and Gradio.

## Description

This project implements a basic RAG pipeline for answering questions based on uploaded documents. It uses PDF loaders, text splitters, embeddings, vector stores, and a conversational chain to provide accurate answers from the provided context.

## Features

- PDF document loading and processing
- Text chunking with configurable splitters
- Embedding generation using pre-trained models
- FAISS vector store for efficient similarity search and retrieval
- LangChain chains for question answering
- Gradio web UI for easy interaction and file uploads
- Modular architecture with separate components for embeddings, loaders, retrievers, etc.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/manideepgembali/Basic-RAG.git
   cd Basic-RAG
   ```

2. Create a virtual environment:

   ```bash
   python -m venv ragproject-env
   # On Windows:
   ragproject-env\Scripts\activate
   # On macOS/Linux:
   source ragproject-env/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Activate the virtual environment (if not already):

   ```bash
   # Windows
   ragproject-env\Scripts\activate
   # macOS/Linux
   source ragproject-env/bin/activate
   ```

2. Run the main application:

   ```bash
   python app.py
   ```

3. Or run the Gradio web UI for a user-friendly interface:

   ```bash
   python ui/ui_gradio.py
   ```

4. Upload a PDF document through the UI and start asking questions!

## Project Structure

```
Basic-RAG/
├── app.py                 # Main application entry point
├── test.py                # Test scripts
├── requirements.txt       # Python dependencies
├── chains/
│   └── rag_chain.py       # LangChain RAG chain implementation
├── data/
│   └── ERP-2008-chapter4.pdf  # Sample PDF document
├── embeddings/
│   └── embedding_model.py # Embedding model utilities
├── loaders/
│   └── pdf_loader.py      # PDF document loader
├── prompts/
│   └── prompts_template.py # Prompt templates for the chain
├── retrivers/
│   └── retriever.py       # Retrieval components
├── splitters/
│   └── text_splitter.py   # Text splitting utilities
├── ui/
│   └── ui_gradio.py       # Gradio web interface
└── vectorstore/
    └── faiss_store.py     # FAISS vector store implementation
```

## Dependencies

Key dependencies include:

- `langchain`: For building the RAG chain
- `langchain-core`: Core LangChain components
- `faiss-cpu`: Vector similarity search
- `gradio`: Web UI framework
- `PyPDF2`: PDF processing
- `sentence-transformers`: For embeddings (if used)

See `requirements.txt` for the complete list.

## How It Works

1. **Document Loading**: PDFs are loaded and parsed into text
2. **Text Splitting**: Documents are split into manageable chunks
3. **Embedding**: Text chunks are converted to vector embeddings
4. **Vector Storage**: Embeddings are stored in FAISS for fast retrieval
5. **Retrieval**: User questions are embedded and similar documents retrieved
6. **Generation**: Retrieved context is used to generate answers via LangChain

## Testing

Run the test script to verify functionality:

```bash
python test.py
```

## Contributing

Contributions are welcome! Please feel free to:

- Open issues for bugs or feature requests
- Submit pull requests for improvements
- Suggest enhancements to the RAG pipeline

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [LangChain](https://langchain.com/)
- Vector search powered by [FAISS](https://github.com/facebookresearch/faiss)
- UI created with [Gradio](https://gradio.app/)
