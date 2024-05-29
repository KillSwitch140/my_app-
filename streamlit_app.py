import streamlit as st
import csv
import os
import pandas as pd
st.title("Interview setup page for Interviewer")
save_dir = 'src/data/originals'
os.makedirs(save_dir, exist_ok=True)

uploaded_file = st.file_uploader("Upload interview file", type=("csv"))

if st.button('Submit', key='submit_button'):
    if uploaded_file is not None:
       
        file_name = uploaded_file.name
        job_position = os.path.splitext(file_name)[0]
    
       
        new_file_path = os.path.join(save_dir, f"{job_position}_dataset.csv")
    
        
        with open(new_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
    
        st.success(f"File has been saved as {new_file_path}")
    
        # Optionally, display the content of the file
        df = pd.read_csv(new_file_path)
        st.write(df)

        

