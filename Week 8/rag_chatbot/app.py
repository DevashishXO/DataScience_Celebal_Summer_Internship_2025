import gradio as gr
from retriever import DocumentRetriever
from generator import AnswerGenerator
import torch

# ---------------- Initializing the components ---------------- #
retriever = DocumentRetriever(
    index_path="vector_store/index.faiss",
    id2doc_path="vector_store/id2doc.pkl"
)

generator = AnswerGenerator(model_name="google/flan-t5-small")

# ---------------- Core RAG pipeline ---------------- #
def rag_pipeline(query, top_k=3):
    # Step 1: Retrieving relevant documents
    retrieved_docs = retriever.retrieve(query, top_k=top_k)
    retrieved_docs = sorted(retrieved_docs, key=lambda x: x[1], reverse=True)
    contexts = [doc for doc, _ in retrieved_docs]

    # Step 2: Generating answer
    answer = generator.generate_answer(question=query, context_docs=contexts)

    # Formatting retrieved documents
    formatted_docs = "\n\n".join([
        f"🔹 **Doc {i+1}** (Score: {round(score, 2)})\n> {doc}"
        for i, (doc, score) in enumerate(retrieved_docs)
    ])

    return answer, formatted_docs


# ---------------- Gradio UI ---------------- #
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        <h1 style="text-align: center;">🤖 Loan Approval RAG Chatbot</h1>
        <p style="text-align: center;">Ask smart questions based on real loan application data. Powered by RAG + Transformers.</p>
        <br>
        """,
    )

    with gr.Row():
        with gr.Column(scale=1):
            question_box = gr.Textbox(
                label="📝 Your Question",
                placeholder="e.g. Do people from urban areas get loans more often?",
                lines=2
            )
            submit_btn = gr.Button("🚀 Generate Answer", variant="primary")
            clear_btn = gr.Button("🗑️ Clear", variant="secondary")
        with gr.Column(scale=2):
            answer_output = gr.Textbox(
                label="✅ Answer", lines=5, interactive=False, show_copy_button=True
            )
            docs_output = gr.Markdown(
                label="📚 Top Retrieved Document Chunks"
            )

    # Define behavior
    submit_btn.click(
        fn=rag_pipeline,
        inputs=[question_box],
        outputs=[answer_output, docs_output]
    )

    clear_btn.click(
        fn=lambda: ("", ""),
        inputs=[],
        outputs=[answer_output, docs_output]
    )

# ---------------- Launch ---------------- #
if __name__ == "__main__":
    demo.launch()
