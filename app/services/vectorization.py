
from app.services.chroma import collection
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

def embed_document(document_text: str):
    # Use OpenAI embeddings for text vectorization
    embeddings = OpenAIEmbeddings()
    vector = embeddings.embed(document_text)
    return vector

def store_document_vector(doc_id: int, vector: list):
    # Store vector in Chroma collection
    collection.add({"id": str(doc_id), "vector": vector})

def vectorize_and_store_doc(doc_id: int, file_path: str):
    try:
        # Read the document text (for simplicity, assuming it's plain text)
        with open(file_path, "r") as file:
            document_text = file.read()

        # Generate embeddings for document text
        vector = embed_document(document_text)

        # Store vector in Chroma collection
        store_document_vector(doc_id, vector)
    except Exception as e:
        print(f"Error during vectorization: {str(e)}")
