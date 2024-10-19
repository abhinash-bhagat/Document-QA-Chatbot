import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from utils.document_handler import get_pdf_text, get_docx_text, get_txt_text

def process_documents(files):
    """Process uploaded documents and return their extracted text."""
    text = ""
    for file in files:
        file_extension = os.path.splitext(file.name)[1].lower()
        
        if file_extension == ".pdf":
            text += get_pdf_text([file])
        elif file_extension == ".docx":
            text += get_docx_text([file])
        elif file_extension == ".txt":
            text += get_txt_text([file])
        else:
            raise ValueError(f"Unsupported file format: {file_extension}")
    
    return text


def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text=text)
    return chunks
