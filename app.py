import streamlit as st

# Page configuration
st.set_page_config(
    page_title="My Streamlit App",
    page_icon="🚀",
    layout="wide"
)

# Title
st.title("🚀 My Streamlit App")

# Sidebar
st.sidebar.header("Settings")
name = st.sidebar.text_input("Enter your name", "")
age = st.sidebar.slider("Select your age", 0, 100, 25)

# Main content
st.header("Welcome Section")

if name:
    st.success(f"Hello {name}! You are {age} years old.")
else:
    st.info("Please enter your name in the sidebar.")

# Button example
if st.button("Click Me"):
    st.balloons()
    st.write("Button clicked!")

# Data example
st.header("Sample Data")

import pandas as pd
import numpy as np

data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["Column 1", "Column 2", "Column 3"]
)

st.dataframe(data)
st.line_chart(data)
