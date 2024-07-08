import streamlit as st
import string

def caesar_cipher(text, shift, alphabet):
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return text.translate(table)

st.title("Text Encryption App")

# Input text area
plaintext = st.text_area("Enter the text to encrypt:", "Hello, World!")

# Sliders for encryption parameters
shift = st.slider("Encryption Key (Shift)", 0, 25, 3)
use_numbers = st.checkbox("Include Numbers", value=True)
use_symbols = st.checkbox("Include Symbols", value=False)

# Create the alphabet based on user choices
alphabet = string.ascii_lowercase
if use_numbers:
    alphabet += string.digits
if use_symbols:
    alphabet += string.punctuation

# Encryption button
if st.button("Encrypt"):
    encrypted_text = caesar_cipher(plaintext.lower(), shift, alphabet)
    st.text_area("Encrypted Text:", encrypted_text, height=100)

# Decryption section
st.subheader("Decryption")
encrypted_input = st.text_area("Enter the text to decrypt:")
decryption_shift = st.slider("Decryption Key (Shift)", 0, 25, 3)

if st.button("Decrypt"):
    decrypted_text = caesar_cipher(encrypted_input, -decryption_shift, alphabet)
    st.text_area("Decrypted Text:", decrypted_text, height=100)
