from langchain_core.prompts import PromptTemplate

def get_prompt_template():
    template = """
You are an intelligent AI assistant.

Answer the user's question ONLY from the provided context.

If the answer is not present in the context, say:
"I don't know based on the provided document."

Do not make up information.
Do not give hallucinated answers.

Context:
{context}

Question:
{question}

Answer:
"""
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=template
    )
    return prompt