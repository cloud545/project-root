
from chromadb import Client

# Initialize Chroma client and configure storage path
client = Client()
collection = client.create_collection(name="knowledge_collection")
