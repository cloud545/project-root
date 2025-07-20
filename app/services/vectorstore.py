
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
import os

# Persistent directory for Chroma DB
PERSIST_DIR = os.getenv("CHROMA_DIR", "storage/chroma")

# Initialize Embedding model
embedding_function = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

# Initialize Chroma vector store
def get_vectorstore():
    return Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function=embedding_function
    )

# Add documents to vectorstore
def add_documents(docs, metadatas=None):
    vs = get_vectorstore()
    vs.add_texts(texts=docs, metadatas=metadatas)
    vs.persist()

# Search documents
def search(query, top_k=5):
    vs = get_vectorstore()
    return vs.similarity_search(query, k=top_k)
