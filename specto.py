import streamlit as st
import re

# Define regular expressions for different patterns
regex_patterns = {
    "Email Addresses": r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
    "Telephone Numbers": r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
    "Dates (MM/DD/YYYY)": r'\b(0?[1-9]|1[0-2])[/-](0?[1-9]|[12][0-9]|3[01])[/-](19|20)?\d{2}\b',
    "URLs": r'(https?://[^\s]+)'
}

# Streamlit app layout
st.title('Regular Expression Pattern Finder')
st.write('Enter your text below and select the pattern you want to search for.')

# Text input box
user_text = st.text_area('Enter text here:', height=200)

# Dropdown menu for selecting pattern
pattern = st.selectbox('Select pattern to search for:', list(regex_patterns.keys()))

# Button to initiate search
if st.button('Find Pattern'):
    if user_text:
        # Find all matches for the selected pattern
        matches = re.findall(regex_patterns[pattern], user_text)
        
        if matches:
            st.write(f"Found {len(matches)} matches for {pattern}:")
            for match in matches:
                st.write(match)
        else:
            st.write(f"No matches found for {pattern}.")
    else:
        st.write("Please enter some text to search.")

# Footer
st.write("Powered by [Streamlit](https://streamlit.io/) and [Python](https://www.python.org/).")
