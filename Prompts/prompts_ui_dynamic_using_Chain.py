import config
import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate, load_prompt

model = ChatOllama(model="smollm2:1.7b", temperature=0.5)

st.header("Research Tool")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis",
    ],
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"],
)
length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphsF)",
        "Long (detailed explanation)",
    ],
)

# template
template = load_prompt("template.json")

# Instead of using the invoke separately, we can make a chain
if st.button("Summarize"):
    chain = template | model
    result = chain.invoke(
        {
            "paper_input": paper_input,
            "style_input": style_input,
            "length_input": length_input,
        }
    )
    st.write(result.content)
