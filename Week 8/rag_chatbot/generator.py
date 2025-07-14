from transformers import pipeline
from typing import List



class AnswerGenerator:
    def __init__(self, model_name: str = "google/flan-t5-small"):
        # Initializing the Hugging Face pipeline with a lightweight model
        self.generator = pipeline("text2text-generation", model=model_name)

    def generate_answer(self, question: str, context_docs: List[str], max_length: int = 256) -> str:
        # Constructing the prompt by combining top-k contexts with the user question
        prompt = "Answer the question based on the context.\nContext: " + " ".join(context_docs) + f"\nQuestion: {question}"

        output = self.generator(prompt, max_length=max_length, truncation=True)[0]['generated_text']
        return output