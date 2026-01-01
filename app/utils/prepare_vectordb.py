import os
# Disable ChromaDB telemetry
os.environ["ANONYMIZED_TELEMETRY"] = "False"

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

# Define the embedding model to use
DEFAULT_EMBEDDING_MODEL = "all-MiniLM-L6-v2"  # A good balance of speed and quality


def extract_pdf_text(pdfs):
    """
    Extract text from PDF documents

    Parameters:
    - pdfs (list): List of PDF documents

    Returns:
    - docs: List of text extracted from PDF documents
    """
    docs = []
    for pdf in pdfs:
        pdf_path = os.path.join("docs", pdf)
        # Load text from the PDF and extend the list of documents
        docs.extend(PyPDFLoader(pdf_path).load())
    return docs


def get_text_chunks(docs):
    """
    Split text into chunks

    Parameters:
    - docs (list): List of text documents

    Returns:
    - chunks: List of text chunks
    """
    # Chunk size is configured to be an approximation to the model limit of 2048 tokens
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=8000, chunk_overlap=800, separators=["\n\n", "\n", " ", ""]
    )
    chunks = text_splitter.split_documents(docs)
    return chunks


def get_vectorstore(pdfs, from_session_state=False):
    """
    Create or retrieve a vectorstore from PDF documents

    Parameters:
    - pdfs (list): List of PDF documents
    - from_session_state (bool, optional): Flag indicating whether to load from session state. Defaults to False

    Returns:
    - vectordb or None: The created or retrieved vectorstore. Returns None if loading from session state and the database does not exist
    """
    load_dotenv()
    # Initialize HuggingFace embeddings - this will download the model on first use
    embedding = HuggingFaceEmbeddings(model_name=DEFAULT_EMBEDDING_MODEL, model_kwargs={'device': 'cpu'})
    if from_session_state and os.path.exists("Vector_DB - Documents"):
        # Retrieve vectorstore from existing one
        vectordb = Chroma(
            persist_directory="Vector_DB - Documents", embedding_function=embedding
        )
        return vectordb
    elif not from_session_state:
        docs = extract_pdf_text(pdfs)
        chunks = get_text_chunks(docs)
        # Create vectorstore from chunks and saves it to the folder Vector_DB - Documents
        vectordb = Chroma.from_documents(
            documents=chunks,
            embedding=embedding,
            persist_directory="Vector_DB - Documents",
        )
        return vectordb
    return None
