# Importing the libraries
import openai
import streamlit as st 
import requests

from streamlit_chat import message

# API Keys 
openai.api_key = st.secrets["api_secret"]

# Creating the function which will generate the calls from the API

def generate_response(prompt):
    completions = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 1024,
        n = 1,
        stop=None,
        temperature = 0.5,       
    )
    
    message = completions.choices[0].text
    return message


st.header("Chatbot : Streamlit + OpenAI")

# Storing the chat
if 'generated' not in st.session_state:
    
    def get_text():
        input_text = st.text_input("You: ", "Hello, hi Chat Assist", key="input")
        st.session_state['generated'] = []            
        return input_text
else: 
    def get_text():
        input_text = st.text_input("You: ", " ", key="input")            
        return input_text
    
    
    
    
    
if 'past' not in st.session_state:
    st.session_state['past'] = []
    
    
def get_text():
    if not st.session_state['generated']:
        input_text = st.text_input("You: ", "Hello, hi Chat Assist", key="input")
    else:
        input_text = st.text_input("You: ", " ", key="input")
    return input_text

user_input = get_text()

if user_input:
    output = generate_response(user_input)
    
    #store the output
    st.session_state.past.append(user_input)
    
    st.session_state.generated.append(output)
    
    
if st.session_state['generated']:
    
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i)),
        message(st.session_state['past'][i], is_user = True, key=str(i) + '_user')