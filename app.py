import streamlit as st
from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence , RunnableParallel
from streamlit_chat import message
from langchain_core.messages import HumanMessage , SystemMessage , AIMessage
from langchain.output_parsers import StructuredOutputParser
from dotenv import load_dotenv
import os
load_dotenv()


def chat_friendly():
    st.set_page_config(page_title='ChatBot' , page_icon="🤖")
    st.title('Personal Chat Friendly AI💬...')
    model = ChatGroq(model="llama-3.1-8b-instant",groq_api_key = os.getenv("GROQ_API_KEY ") ,temperature=0.8)
    
    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="You are a helpful AI assistant")
        ]
        
    user_input = st.chat_input('Enter here')
    if user_input:
        # message(user_input , is_user=True)
        st.session_state.messages.append(HumanMessage(content=user_input))
        with st.spinner('Thinking.....'):
            
            response = model(st.session_state.messages)
            st.session_state.messages.append(AIMessage(content=response.content))
            
        messages = st.session_state.get('messages' , [])
        for i , msg in enumerate(messages[1:]):
            if i%2 == 0:
                message(msg.content , is_user=True , key=f"{i} _user")
            else:
                message(msg.content , is_user=False , key=f"{i} _AI")
                



if __name__=="__main__":
    chat_friendly()
 