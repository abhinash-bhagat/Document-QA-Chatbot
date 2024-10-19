from PyPDF2 import PdfReader
from docx import Document


# Function to read PDFs
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Function to read DOCS
def get_docx_text(docx_docs):
    """Extract text from Word (.docx) files."""
    text = ""
    for docx in docx_docs:
        doc = Document(docx)
        for para in doc.paragraphs:
            text += para.text
    return text


# Function to read TXT
def get_txt_text(txt_docs):
    """Extract text from plain text (.txt) files."""
    text = ""
    for txt in txt_docs:
        text += txt.read().decode("utf-8")
    return text