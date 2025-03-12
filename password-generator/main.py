import streamlit as st  
import random  
import string  

# Function to generate password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  

    if use_digits:
        characters += string.digits  

    if use_special:
        characters += (
            string.punctuation
        )  
        
    return "".join(random.choice(characters) for _ in range(length))


st.set_page_config(
    page_title="Password Generator",
    page_icon="🔐",
    layout="centered"
)

st.markdown("""
<style>
    .main {
        padding: 2rem;
        border-radius: 10px;
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
    }
    .password-output {
        padding: 1rem;
        background-color: white;
        border-radius: 5px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

st.title("🔐 Password Generator")
st.markdown("Generate strong and secure passwords with customizable options.")

with st.container():
    length = st.slider("Password Length", min_value=6, max_value=32, value=12)
    
    col1, col2 = st.columns(2)
    with col1:
        use_digits = st.checkbox("Include Numbers", value=True)
    with col2:
        use_special = st.checkbox("Include Special Characters", value=True)

    if st.button("Generate Password 🎲"):
        password = generate_password(length, use_digits, use_special)
        st.markdown("### Your Generated Password:")
        st.code(password, language="")
        
        strength = "Strong 💪" if length >= 12 and use_digits and use_special else "Medium 👍" if length >= 8 else "Weak 😕"
        st.info(f"Password Strength: {strength}")
        
        st.markdown("""
        #### Password Tips:
        - Keep your password safe and don't share it
        - Use different passwords for different accounts
        - Consider using a password manager
        """)