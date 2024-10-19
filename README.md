# Document QA Chatbot

## Project Overview

The Document QA Chatbot is an interactive application built using **Streamlit** and **Langchain**. It allows users to upload documents (PDFs, TXT files, Word files) and ask questions based on the content of those documents. Utilizing advanced natural language processing techniques, the chatbot provides accurate answers and can also collect user information for scheduling appointments or follow-ups.

## Features

- **Document Upload**: Users can upload multiple PDF and TXT documents.
- **Question Answering**: Ask questions related to the content of the uploaded documents.
- **User Interaction**: Collect user information (name, email, phone number, appointment date) for follow-up.
- **Session Management**: Maintains conversation state to provide a smooth user experience.
- **Error Handling**: Validates user inputs to ensure data integrity and improve user experience.
- **Embeddings and Vector Store**: Uses Google Generative AI embeddings for efficient document search.

## Technologies Used

- **Python**: Programming language used for backend logic.
- **Streamlit**: Framework for building the web application.
- **Langchain**: For building the conversational chain and managing prompts.
- **FAISS**: A library for efficient similarity search and clustering of dense vectors.
- **Google Generative AI**: For embeddings to enhance the question-answering capabilities.

## Installation

To run the Document QA Chatbot locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/document-qa-chatbot.git
   cd document-qa-chatbot
2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate` 
3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Run the application:**
   ```bash
   streamlit run app.py
