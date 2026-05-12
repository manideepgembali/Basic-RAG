import gradio as gr

from loaders.pdf_loader import load_pdf
from splitters.text_splitter import split_documents
from embeddings.embedding_model import get_embedding_model
from vectorstore.faiss_store import create_vector_store
from retrivers.retriever import create_retriever
from prompts.prompts_template import get_prompt_template
from chains.rag_chain import get_llm, create_rag_chain


# Global RAG chain
rag_chain = None


def process_pdf(pdf_file):
    """
    Processes uploaded PDF and creates RAG pipeline
    """

    global rag_chain

    try:

        # Load PDF
        documents = load_pdf(pdf_file.name)

        # Split documents
        split_docs = split_documents(documents)
        
        print(type(split_docs))
        print(type(split_docs[0]))

        # Embedding model
        embedding_model = get_embedding_model()

        # Create vector store
        vector_store = create_vector_store(
            split_docs,
            embedding_model
        )

        # Create retriever
        retriever = create_retriever(vector_store)

        # Prompt template
        prompt = get_prompt_template()

        # LLM
        llm = get_llm()

        # Create RAG chain
        rag_chain = create_rag_chain(
            retriever,
            prompt,
            llm
        )

        return "PDF processed successfully. You can now ask questions."

    except Exception as e:
        return f"Error processing PDF: {e}"


def ask_question(question):
    """
    Handles user questions
    """

    global rag_chain

    try:

        if rag_chain is None:
            return "Please upload and process a PDF first."

        response = rag_chain.invoke(question)

        return response

    except Exception as e:
        return f"Error generating response: {e}"


# Create Gradio UI
with gr.Blocks() as demo:

    gr.Markdown("# RAG Application using LangChain + Gemini")

    with gr.Row():

        pdf_input = gr.File(
            label="Upload PDF",
            file_types=[".pdf"]
        )

    process_button = gr.Button("Process PDF")

    process_output = gr.Textbox(
        label="Processing Status"
    )

    process_button.click(
        fn=process_pdf,
        inputs=pdf_input,
        outputs=process_output
    )

    gr.Markdown("## Ask Questions")

    question_input = gr.Textbox(
        label="Enter your question"
    )

    ask_button = gr.Button("Ask Question")

    answer_output = gr.Textbox(
        label="AI Response",
        lines=10
    )

    ask_button.click(
        fn=ask_question,
        inputs=question_input,
        outputs=answer_output
    )


# Launch app
demo.launch()