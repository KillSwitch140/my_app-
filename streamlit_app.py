import streamlit as st
import streamlit_authenticator as stauth
st.title('🎈 App Name')

st.write('Hello world!')
hashed_passwords = stauth.Hasher(['abc', 'def']).generate()
print(hashed_passwords)
