import streamlit as st

# Basic Streamlit app to test functionality
st.title('Regular Expression Pattern Finder')
st.write('Enter your text below and select the pattern you want to search for.')

# Text input box
user_text = st.text_area('Enter text here:', height=200)

# Dropdown menu for selecting pattern
pattern = st.selectbox('Select pattern to search for:', ["Email Addresses", "Telephone Numbers", "Dates (MM/DD/YYYY)", "URLs"])

# Button to initiate search
if st.button('Find Pattern'):
    st.write('Button pressed.')
    st.write(f'Text entered: {user_text}')
    st.write(f'Pattern selected: {pattern}')
