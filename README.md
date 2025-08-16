# 🤖 arXiv Expert Chatbot (Computer Science Research Assistant)

This is a domain-specific intelligent chatbot trained on the arXiv scientific papers dataset (Computer Science domain). It helps users explore and retrieve relevant research papers based on their query using semantic similarity and vector search.

> 🚀 Developed as part of internship project at **NullClass Edtech Pvt. Ltd.**

---

## 🔍 Features

- Ask research questions and get **top 5 relevant papers**
- View **title, categories, and abstract** of each paper
- Uses **Sentence Transformers** for semantic embedding
- Efficient search using **FAISS** (Facebook AI Similarity Search)
- Built with an elegant **Streamlit UI**
- Lightweight, responsive, and easy to deploy

---

## 📦 Dataset Requirement

To keep the repository size under 25MB, large files are not included. You need to manually download the dataset:

- 🔗 Dataset: [arxiv-metadata-oai-snapshot.json](https://www.kaggle.com/datasets/Cornell-University/arxiv)
- 🔗 cs_data.pkl file: [https://www.kaggle.com/datasets/prasadpardeshi07/arxiv-expert-chatbot-data]

- Source: **Kaggle** (free to download)
- Size: ~2.4 GB & ~1.2 GB
**Download These two files**
  
  **After downloading this repository as a ZIP and extracting it, move this two files into the root project directory, like this:**
  
  **📂 Project Folder Structure**  

| File/Folder       | Description                                    |
|-------------------|------------------------------------------------|
| `UI.py`           | Main Streamlit application file                |
| `requirements.txt`| List of required Python dependencies           |
| `cs_data.pkl` ✅   | Data file (download separately & place here)   |
| `cs_index.faiss` ✅| FAISS index file                             |

  

---


## 💻 How to Run the Chatbot
1. Install dependencies :- pip install -r requirements.txt
 
2.Launch Streamlit app :- streamlit run UI.py

3.You’ll see a clean UI like this:-
<img width="1920" height="1080" alt="Screenshot 2025-08-08 002738" src="https://github.com/user-attachments/assets/409eb290-6e74-4174-affb-a9e42f585003" />

## 📝 Technologies Used
Python 🐍

Streamlit 🌐

FAISS (Facebook AI) 📦

SentenceTransformers (MiniLM) 🔠

Pandas, NumPy, Scikit-learn 📊

## 📁 Project Structure
.
├── UI.py                      # Streamlit chatbot UI
├── arxiv_expert_chatbot.ipynb # Main notebook for preprocessing + embeddings
├── cs_index.faiss            # FAISS index (generated)
├── cs_data.pkl               # Encoded data (generated, not uploaded)
├── requirements.txt          # Project dependencies
└── README.md                 # Project overview

## 🏢 Internship Credit
This project was developed as part of a 2-month internship at:

NullClass Edtech Pvt. Ltd.
📅 July 2025 – Sept 2025

## 📬 Contact
Prasad Pardeshi
GitHub: @PrasadPardeshi20
Email : prasadpardeshi480@gmail.com
