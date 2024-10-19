from langchain.prompts import PromptTemplate  # Import PromptTemplate for creating custom prompts
from langchain.chains.question_answering import load_qa_chain  # Import load_qa_chain for loading a QA chain
from langchain_google_genai import ChatGoogleGenerativeAI  # Import the generative AI model from LangChain

# Setup the QA chain using the Google Generative AI model
def get_conversational_chain():
    # Define the prompt template for the QA chain
    prompt_template = """
    Answer the question based on the context provided. If the answer is not in the context, say 'Answer not in context.'.
    Context: \n{context}\n
    Question: \n{question}\n
    Answer:
    """
    # Instantiate the generative AI model with specified parameters
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    
    # Create a prompt using the defined template and specify input variables
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    
    # Load the QA chain with the specified language model and prompt
    return load_qa_chain(llm=model, chain_type="stuff", prompt=prompt)

# Get an answer from the QA chain based on the provided documents and user question
def get_answer(docs, user_question):
    # Retrieve the QA chain
    chain = get_conversational_chain()
    
    # Execute the chain with the input documents and user question, returning the output text
    return chain({"input_documents": docs, "question": user_question})["output_text"]
