import streamlit as st
import pandas as pd
import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

st.set_page_config(page_title="arXiv Research Assistant", page_icon="🔍", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_pickle("cs_data.pkl")
    index = faiss.read_index("cs_index.faiss")
    return df, index

df, index = load_data()
model = SentenceTransformer("all-MiniLM-L6-v2")

st.markdown("""
    <style>
    .stApp {
        background-color: #ffffff;
        font-family: Arial, sans-serif;
    }
    .title-style {
        font-size: 2.5em;
        font-weight: 700;
        color: #222222;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle-style {
        font-size: 1.1em;
        color: #555555;
        text-align: center;
        margin-bottom: 30px;
    }
    .query-box textarea {
        font-size: 1.1em !important;
        border-radius: 0.5rem !important;
        border: 1px solid #ccc !important;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 0.9em;
        color: #999999;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title-style'>🔍 arXiv Expert Chatbot</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle-style'>Ask research queries and discover relevant computer science papers from arXiv.</div>", unsafe_allow_html=True)

query = st.text_input("Enter your research query:", key="query", help="Type any research topic or question to find matching papers.")

if query:
    with st.spinner("Searching for papers..."):
        query_embedding = model.encode([query])
        distances, indices = index.search(np.array(query_embedding).astype("float32"), k=5)

        st.markdown("### 📝 Top 5 Relevant Papers")
        for i in indices[0]:
            paper = df.iloc[i]
            st.markdown(f"#### {paper['title']}")
            st.markdown(f"**Categories:** `{paper['categories']}`")
            st.markdown(f"**Abstract:** {paper['abstract']}")
            st.markdown("---")

st.markdown("""
<div class='footer'>
    © 2025 Internship Project | Developed by Prasad Pardeshi | NullClass Edtech Pvt.Ltd
</div>
""", unsafe_allow_html=True)
