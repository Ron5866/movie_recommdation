# 🎬 Movie Recommendation System

A **Movie Recommendation System** built with **Machine Learning (Cosine Similarity)** and **Streamlit** that suggests movies based on user preferences.  
It fetches additional details like posters, genres, and ratings using the **OMDb API**.

---

## 🚀 Features

- 🔍 Search for any movie by name
- 🎯 Get similar movie recommendations using **Cosine Similarity**
- 🖼️ Display movie posters, genre, and ratings via **OMDb API**
- ⚡ Fast and interactive interface powered by **Streamlit**
- 🧠 Uses a **content-based filtering approach**

---

## 📸 Demo

> _Add a screenshot or a short GIF of your app here for better presentation._

---

## 🛠️ Tech Stack

- **Python**
- **Pandas / NumPy**
- **Scikit-learn**
- **Streamlit**
- **OMDb API**
- **Cosine Similarity (Content-Based Filtering)**



## ⚙️ Installation & Setup

1️⃣ **Clone the repository**
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
2️⃣ Create and activate a virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Get OMDb API Key

Visit OMDb API and get a free API key.

Create a .env file and add your API key:

OMDB_API_KEY=your_api_key_here

5️⃣ Run the app
streamlit run app.py



