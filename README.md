
# 📚 RAG PDF Chatbot (LangChain + Gemini + Hugging Face)

A simple, powerful chatbot app built using LangChain, Streamlit, Google Gemini Embeddings, and HuggingFace Hub models like `flan-t5-large`. This app lets you **upload multiple PDF files**, process them into chunks, generate embeddings, and ask questions in natural language—getting **context-aware answers** from your documents in real-time.

---

## 🧠 What is RAG?

**RAG** (Retrieval-Augmented Generation) is an architecture that combines:
- 🔍 **Retrieval**: Searching relevant chunks from a document database (vector store)
- 🤖 **Generation**: Answering your question using a language model (LLM), grounded in the retrieved context

---

## ✨ Features

- Upload multiple PDFs and query them
- Uses Google Gemini API for custom embeddings
- FAISS as an in-memory vector store
- Conversational memory for chat history
- Works with Hugging Face LLMs (like `flan-t5-large`)
- Clean web interface via Streamlit

---

## 📁 Project Structure

```
rag_pdf_chatbot/
│
├── app.py                     # Streamlit app
├── templates.py               # HTML/CSS templates for chatbot messages
├── .env                       # Contains GEMINI_API_KEY, OPEN_AI_API_KEY and HF_API_KEY
├── requirements.txt           # All dependencies
├── test.py                    # to test api key properly loading or not
└── README.md                  # You're reading it!
```

---

## 🛠️ Setup Instructions

### ✅ Prerequisites

- Python 3.10
- [HuggingFace API Key](https://huggingface.co/settings/tokens)
- [Google AI Studio Gemini API Key](https://makersuite.google.com/app)

### 🔧 Create Environment (Optional via Conda)

```bash
# Open terminal or Anaconda Prompt
conda create -n rag310 python=3.10
conda activate rag310
```

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔑 Create `.env` File

```env
GEMINI_API_KEY=your_google_gemini_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_key
```

---

## 🚀 Run the App

```bash
streamlit run app.py
```

Then go to `http://localhost:8501` in your browser.

---

## 🖼️ Screenshots

> Add screenshots of your UI here (upload images to GitHub or embed directly)

---

## 💡 Example Models

- `google/flan-t5-large` via Hugging Face
- You can replace it with other HuggingFace-supported models

---

## 🔌 Technologies Used

- **Streamlit** – Web UI
- **LangChain** – Orchestration
- **FAISS** – Vector DB
- **Gemini API** – Embeddings
- **HuggingFace** – Language model inference

---

## 📃 License

MIT License

---

## 🙌 Credits

Built with ❤️ by Praveen Roy

---
