import config
import streamlit as st
from langchain_ollama import ChatOllama

model = ChatOllama(
    model="smollm2:1.7b", temperature=0, num_predict=512
)  # num_predict --> output tokens

st.header("Research Tool")
user_input = st.text_input("Enter your prompt")

if st.button("Summarize"):
    result = model.invoke(user_input)
    st.text(result.content)