import streamlit as st


with st.sidebar:
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/pages/1_File_Q%26A.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("Interview setup page for Interviewer")

uploaded_file = st.file_uploader("Upload interview file", type=("csv"))

question = st.text_input(
    "Ask something about the article",
    placeholder="Can you give me a short summary?",
    disabled=not uploaded_file,
)



