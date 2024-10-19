import streamlit as st  # Import Streamlit for building the web application
from vector_store import load_vector_store  # Import function to load vector store for document retrieval
from conversational_chain import get_answer  # Import function to get answers from the conversational model
from utils.validations import extract_date, validate_email, validate_phone_number  # Import validation functions

# Handle user's question input and provide appropriate response
def handle_user_input(user_question):
    # Check if the user question contains keywords indicating a request for contact information
    if "hi" in user_question.lower() or "hello" in user_question.lower():
        st.write("Reply: Hello! Please upload the document and start asking the questions.")
    elif "call" in user_question.lower() or "contact" in user_question.lower() or "email me" in user_question.lower() or "appointment" in user_question.lower():
        collect_user_information()  # Call function to collect user's contact information
    else:
        # Proceed with normal question-answer flow
        vector_store = load_vector_store()  # Load vector store for similarity search
        docs = vector_store.similarity_search(user_question)  # Find relevant documents based on user question
        response = get_answer(docs, user_question)  # Get the answer from the conversational model
        st.write("Reply: ", response)  # Display the bot's reply

# Collect user information (name, phone number, email)
def collect_user_information():
    # Initialize session state if not already done
    if "step" not in st.session_state:
        st.session_state.step = 1  # Start at step 1
        st.session_state.user_info = {  # Initialize a dictionary to store user info
            "name": None,
            "email": None,
            "phone": None,
            "date": None
        }

    # Step 1: Ask for Name
    if st.session_state.step == 1:
        st.write("Bot: We can schedule a call for you. Please tell us your details.\n What is your name?") # Prompt user for their name
        
        name_input = st.text_input("You: ", key="name_input")  # Input field for user name

        if name_input:  # If user provided their name
            st.session_state.user_info["name"] = name_input  # Store name in session state
            st.session_state.step = 2  # Move to the next step
            st.rerun()  # Rerun the app to process the next step

    # Step 2: Ask for Email
    elif st.session_state.step == 2:
        st.write(f"Bot: Okay {st.session_state.user_info['name']}, please tell us your email address.")  # Personalize the prompt
        email_input = st.text_input("You: ", key="email_input")  # Input field for user email

        # Validate email input
        if email_input and validate_email(email_input):  # If a valid email is provided
            st.session_state.user_info["email"] = email_input  # Store email in session state
            st.session_state.step = 3  # Move to the next step
            st.rerun()  # Rerun the app to process the next step
        elif email_input:
            st.error("Please enter a valid email address.")  # Show error for invalid email

    # Step 3: Ask for Phone Number
    elif st.session_state.step == 3:
        st.write("Bot: Please tell us your phone number (e.g., +1234567890):")  # Prompt for phone number
        phone_input = st.text_input("You: ", key="phone_input")  # Input field for user phone number

        # Validate phone number input
        if phone_input and validate_phone_number(phone_input):  # If a valid phone number is provided
            st.session_state.user_info["phone"] = phone_input  # Store phone number in session state
            st.session_state.step = 4  # Move to the next step
            st.rerun()  # Rerun the app to process the next step
        elif phone_input:
            st.error("Please enter a valid phone number.")  # Show error for invalid phone number

    # Step 4: Ask for Appointment Date
    elif st.session_state.step == 4:
        st.write("Bot: When would you like to schedule the appointment? (Tomorrow or Next week or YYYY-MM-DD):")  # Prompt for date
        date_input = st.text_input("You: ", key="date_input")  # Input field for user appointment date

        if date_input:  # If user provided a date
            parsed_date = extract_date(date_input)  # Parse the date input
            if parsed_date:  # If parsing was successful
                st.session_state.user_info["date"] = parsed_date  # Store the date in session state
                st.session_state.step = 5  # Move to the next step
                st.rerun()  # Rerun the app to process the next step
            else:
                st.error("Please enter a valid date in YYYY-MM-DD format or a valid natural language date.")  # Show error for invalid date

    # Step 5: Summary and Confirmation
    elif st.session_state.step == 5:
        st.write("Bot: Great! Here's the information you've provided:")  # Summarize collected information
        st.write(f"**Name:** {st.session_state.user_info['name']}")  # Display user's name
        st.write(f"**Email:** {st.session_state.user_info['email']}")  # Display user's email
        st.write(f"**Phone:** {st.session_state.user_info['phone']}")  # Display user's phone number
        st.write(f"**Appointment Date:** {st.session_state.user_info['date']}")  # Display appointment date

        # Confirmation button for user
        if st.button("Confirm"):
            st.success("Your appointment has been successfully booked!")  # Show success message
            # Clear session state for new conversations
            st.session_state.step = 1  # Reset step to 1
            st.session_state.user_info = {  # Clear user info for next interaction
                "name": None,
                "email": None,
                "phone": None,
                "date": None
            }