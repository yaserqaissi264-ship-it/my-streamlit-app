import streamlit as st

st.set_page_config(page_title="My App", layout="wide")

st.title("Welcome to My Streamlit App")
st.write("This is a simple Streamlit application example.")

# Sidebar
st.sidebar.header("Settings")
name = st.sidebar.text_input("Enter your name:", "User")
age = st.sidebar.slider("Select your age:", 0, 100, 25)

# Main content
st.subheader(f"Hello, {name}!")
st.write(f"You are {age} years old.")

# Add some interactive elements
col1, col2 = st.columns(2)
with col1:
    st.metric("Age", age)
with col2:
    st.metric("Name Length", len(name))

# Button
if st.button("Click me!"):
    st.balloons()
    st.success("You clicked the button!")