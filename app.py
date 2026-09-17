import streamlit as st

st.set_page_config(page_title="My Webpage", layout="wide")

# This reads your HTML file and displays it inside your Streamlit app
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

st.components.v1.html(html_code, height=800, scrolling=True)
