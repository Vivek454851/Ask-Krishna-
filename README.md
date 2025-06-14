
# 🕉️ Ask Krishna – Bhagavad Gita Chatbot

An AI-powered chatbot built using Streamlit and Sentence Transformers that helps users ask questions and receive guidance inspired by the **Bhagavad Gita**. Just enter your question in natural language, and the system retrieves the most relevant verse with its English, Sanskrit, and Hindi meanings.

---

## ✨ Features

- 🔍 **Semantic Search** on Gita verses using Sentence Transformers
- 🧠 **Intelligent Matching** with cosine similarity
- 📖 Provides **Chapter and Verse**, along with:
  - English Translation
  - Hindi Meaning
  - Sanskrit Shloka
- 🎨 Beautiful and Krishna-themed UI
- 📦 Powered by Streamlit for rapid development

---

## 📸 Demo

![Ask Krishna UI Screenshot](screenshot.png) <!-- Replace with actual screenshot path -->

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **ML/NLP**: [Sentence-Transformers](https://www.sbert.net/) (`all-MiniLM-L6-v2`)
- **Data Handling**: Pandas, OpenPyXL
- **Similarity Metric**: Cosine Similarity from scikit-learn

---

## 📂 Folder Structure
Ask-Krishna-Chatbot/
├── bhagavad-gita.xlsx # Bhagavad Gita dataset (with multiple languages)
├── app.py # Main Streamlit app
├── requirements.txt # Python dependencies
└── README.md # Project documentation

