import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
import os

st.set_page_config(page_title="KPilot - Kafka Copilot", layout="wide")
st.title("🚀 KPilot – Your Kafka Copilot")
st.markdown("Ask questions about Kafka CLI, tuning, configs – trained on real Kafka docs!")

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

# Load Kafka documentation
def load_docs():
    loader = DirectoryLoader('kafka_docs', glob="**/*.pdf", loader_cls=PyPDFLoader)
    docs = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    return text_splitter.split_documents(docs)

@st.cache_resource
def create_vectorstore():
    docs = load_docs()
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    return FAISS.from_documents(docs, embeddings)

db = create_vectorstore()

question = st.text_input("📥 Ask your Kafka question:")
if question:
    retriever = db.as_retriever()
    llm = OpenAI(openai_api_key=OPENAI_API_KEY)
    from langchain.chains import RetrievalQA
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    response = qa.run(question)
    st.write("💡", response)
