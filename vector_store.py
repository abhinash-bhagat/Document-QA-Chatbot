from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

def setup_vector_store(text_chunks):
    """
    Set up a FAISS vector store from given text chunks.
    
    Args:
        text_chunks (list): List of strings to embed and store.
    """
    # Create embeddings for the text chunks using the specified model
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    
    # Initialize a FAISS vector store with the text chunks and their embeddings
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    
    # Save the vector store locally for later use
    vector_store.save_local("faiss_index")

def load_vector_store():
    """
    Load the FAISS vector store from local storage.
    
    Returns:
        FAISS: Loaded vector store object.
    """
    # Create embeddings again for loading the vector store
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    
    # Load the previously saved FAISS index and allow dangerous deserialization
    return FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
