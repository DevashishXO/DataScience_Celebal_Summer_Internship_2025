# Loan Approval RAG Chatbot

> A Retrieval-Augmented Generation (RAG) based intelligent chatbot that answers questions using real-world loan application records. Built using **FAISS**, **Hugging Face Transformers**, and **Gradio**. Lightweight and optimized for free hosting on Hugging Face Spaces.

---

## Screenshots

| Home Interface | Answer Example |
|----------------|----------------|
| ![Home UI](screenshots/home.png) | ![Answer UI](screenshots/answer.png) |

---

## Author

**Devashish Nagpal**  
*B.Tech CSE | AI/ML Researcher | Intern at Celebal Technologies*

---

## Project Description

This project implements a **Question-Answering chatbot** over structured loan application data using a **Retrieval-Augmented Generation** (RAG) approach. Users can ask natural-language questions (e.g., _"Do unmarried women get approved for loans?"_), and the bot will:

1. Retrieve the **most relevant loan entries** from the dataset using FAISS vector search.
2. Generate a **natural language answer** using a small language model (like `flan-t5-small`), grounded in the retrieved evidence.
3. Show **top-k matching document chunks** as sources used in the answer.

It is optimized to **run locally or on Hugging Face Spaces for free**, without paid API dependencies or large model usage.

---

## Tech Stack

| Component       | Tool/Library                    |
|----------------|----------------------------------|
| Embeddings      | `sentence-transformers`         |
| Vector Index    | `faiss`                         |
| Answer Generation | `transformers (flan-t5-small)` |
| Web UI          | `gradio`                        |
| Dataset         | [Loan Approval Dataset (Kaggle)](https://www.kaggle.com/datasets/sonalisingh1411/loan-approval-prediction) |

---

## Features

- **Fast FAISS retrieval** from document embeddings
- **Transparent answers** with reasoning and supporting evidence
- **Simple UI** using Gradio (mobile and desktop friendly)
- **Top-k source documents shown**
- Lightweight for local deployment or Hugging Face Spaces

---

## 🚀 How to Run the App Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/DevashishXO/DataScience_Celebal_Summer_Internship_2025
   cd .\DataScience_Celebal_Summer_Internship_2025\
   cd .\Week 8\
   ```
2. **Set up a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare the dataset**
   - Place the `train.csv` and file in the `data/` directory.
   - Run the notebook `assignment_week8.ipynb` to preprocess the data and create the FAISS index.
   - This will generate the vector store files in `rag_chatbot/vector_store/`.

5. **Run the app**
   ```bash
   cd .\rag_chatbot\
   python .\app.py
   ```

6. **Access the app**
   - Open your browser and go to `http://127.0.0.1:7860`
   - You should see the chatbot interface where you can ask questions about loan approvals.
   - Example query: "What kind of applicants get approved for a loan?" ; "What kind of people usually get rejected?" ; "Does credit history affect loan approval?"

## File Structure
```
Week_8/
├── assignment_week8.ipynb
├── README.md
├── requirements.txt
└── rag_chatbot/
    ├── app.py
    ├── retriever.py
    ├── generator.py
    ├── utils.py
    ├── data/
    │   ├── train.csv
    │   └── test.csv
    └── vector_store/
        ├── index.faiss
        └── id2doc.pkl
```