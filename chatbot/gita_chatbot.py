# pip install streamlit pandas sentence-transformers scikit-learn openpyxl

import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load Gita dataset
@st.cache_data
def load_data():
    df = pd.read_excel("bhagavad-gita.xlsx", sheet_name="Bhagavad-Gita")
    df.rename(columns={"Enlgish Translation": "English"}, inplace=True)
    df["English"] = df["English"].fillna("")
    return df

# Load sentence transformer model
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

# Compute embeddings (not cached)
def get_embeddings(texts, model):
    return model.encode(texts, convert_to_tensor=True)

# --- Streamlit UI ---
st.title("🕉️ Ask Krishna" )
st.markdown("Ask anything based on the teachings of the Bhagavad Gita.")

# Load data and model
df = load_data()
model = load_model()
texts = df["English"].tolist()
embeddings = get_embeddings(texts, model)

# Input question
user_question = st.text_input("🙏 Enter your question:")

if user_question:
    question_embedding = model.encode([user_question], convert_to_tensor=True)
    scores = cosine_similarity(question_embedding.cpu(), embeddings.cpu())[0]
    best_idx = scores.argmax()

    result = df.iloc[best_idx]
    
    st.markdown(f"### 📖 Chapter {result['Chapter']} – Verse {result['Verse']}")
    st.success(result['English'])
    
    with st.expander("Show Sanskrit & Hindi Translation"):
        st.write(f"**Sanskrit:** {result.get('Sanskrit Anuvad', 'N/A')}")
        st.write(f"**Hindi:** {result.get('Hindi Anuvad', 'N/A')}")
