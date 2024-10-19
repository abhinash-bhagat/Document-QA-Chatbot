import streamlit as st  # Import the Streamlit library for building the web app
from utils.document_processing import process_documents, get_text_chunks  # Import functions for processing documents
from conversational_chain import get_answer  # Import the function to get answers from the chatbot
from vector_store import setup_vector_store  # Import the function to set up the vector store for document retrieval
from form_handlers import handle_user_input  # Import the function for handling user input

def main():
    # Set up the page configuration for the Streamlit app
    st.set_page_config("Document QA Chatbot")
    
    # Display the header of the app
    st.header("Document QA Chatbot")

    # Create a text input field for users to ask questions
    user_question = st.text_input("Ask your question")
    
    # If the user has entered a question, handle the input
    if user_question:
        handle_user_input(user_question)  # Process the user's question

    # Create a sidebar for additional functionalities
    with st.sidebar:
        st.title("Menu:")  # Set the title for the sidebar
        # Allow users to upload multiple PDF files
        pdf_docs = st.file_uploader("Upload your pdf files", accept_multiple_files=True)
        
        # Button to submit and process the uploaded documents
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):  # Show a loading spinner while processing
                # Process the uploaded documents to extract raw text
                raw_text = process_documents(pdf_docs)
                # Break the raw text into manageable chunks
                text_chunks = get_text_chunks(raw_text)
                # Set up a vector store with the text chunks for efficient querying
                setup_vector_store(text_chunks)
                # Notify the user that the documents have been processed successfully
                st.success("Documents processed successfully")

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    main()  # Call the main function to run the app
