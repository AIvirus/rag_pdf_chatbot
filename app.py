import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
import requests
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import HuggingFaceHub
from templates import css, bot_template, user_template
import os
# from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
# from langchain.chat_models import ChatOpenAI

# Google Gemini Embeddings using REST API
def get_gemini_embeddings(text_chunks):
    api_key = os.getenv("GEMINI_API_KEY")
    endpoint = "https://generativelanguage.googleapis.com/v1beta/models/embedding-001:embedContent?key=" + api_key

    embeddings = []
    
    for chunk in text_chunks:
        payload = {
            "model": "embedding-001",
            "content": {
                "parts": [{"text": chunk}]
            }
        }
        response = requests.post(endpoint, json=payload)
        result = response.json()
        embedding = result['embedding']['values']
        embeddings.append(embedding)
    return embeddings

# Create FAISS vectorstore with Gemini embeddings
def get_vectorstore(text_chunks):
    from langchain.vectorstores import FAISS
    from langchain.schema.embeddings import Embeddings

    class GeminiEmbeddingFunction(Embeddings):
        def embed_documents(self, texts):
            return get_gemini_embeddings(texts)

        def embed_query(self, text):
            return get_gemini_embeddings([text])[0]

    embedding_model = GeminiEmbeddingFunction()
    
    vectorstore = FAISS.from_texts(text_chunks, embedding_model)
    # embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    # vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    
    return vectorstore


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=800, chunk_overlap=200, length_function=len
    )
    return text_splitter.split_text(text)

# HuggingFace Inference API (e.g., flan-t5-xxl, flan-t5-large, etc)
def get_conversation_chain(vectorstore):
    llm = HuggingFaceHub(
        repo_id="google/flan-t5-large",
        model_kwargs={"temperature": 0.5, "max_length": 512}
    )
    # llm = ChatOpenAI()
    # llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3, google_api_key=os.getenv("GEMINI_API_KEY"))
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm, retriever=vectorstore.as_retriever(), memory=memory
    )
    return chain

def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, msg in enumerate(st.session_state.chat_history):
        template = user_template if i % 2 == 0 else bot_template
        st.write(template.replace("{{MSG}}", msg.content), unsafe_allow_html=True)

def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with PDFs (Gemini + HF API)", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Chat with multiple PDFs :books:")
    user_question = st.text_input("Ask a question about your documents:")
    if user_question:
        handle_userinput(user_question)

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload PDFs & click Process", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vectorstore = get_vectorstore(text_chunks)
                st.session_state.conversation = get_conversation_chain(vectorstore)

if __name__ == "__main__":
    main()
