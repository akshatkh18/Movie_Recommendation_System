# 🎬 Movie Recommendation System

## Demo

Live App: *[Live Demo link here](https://huggingface.co/spaces/akshat18/movie-recommendation)*

---

## 📌 Overview

This project is a **content-based movie recommendation system** that suggests similar movies based on user selection.
It uses **cosine similarity** on processed movie features to find the most relevant recommendations.

---

## ⚙️ Features

* Recommend top similar movies instantly
* Clean and simple UI using Streamlit
* Fast retrieval using precomputed similarity matrix
* Uses real-world movie dataset (TMDB 5000)

---

## 🧠 How It Works

1. Movie data is preprocessed (genres, keywords, cast, crew)
2. Features are combined into a single text vector
3. Text is converted using **CountVectorizer / TF-IDF**
4. Cosine similarity is calculated between all movies
5. For a selected movie, top similar movies are returned

---

## 🛠 Tech Stack

* **Python**
* **Pandas, NumPy**
* **Scikit-learn**
* **Streamlit**

---

## 📂 Project Structure

```
movie-recommendation/
│
├── app.py                 # Streamlit UI
├── recommender.py         # Recommendation logic
├── requirements.txt       # Dependencies
├── .gitignore             # Ignored files
├── README.md              # Project documentation
```

---

## ⚡ Installation & Run Locally

### 1. Clone the repository

```
git clone https://github.com/your-username/Movie_Recommendation_System.git
cd Movie_Recommendation_System
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the app

```
streamlit run app.py
```

---

## 📊 Dataset

Dataset is not included in this repository due to size limitations.

You can download it from:

* TMDB 5000 Movies Dataset (Kaggle)

---

## 🚧 Limitations

* Only content-based filtering 
* Recommendations depend on feature engineering quality
* Cold start problem for new movies

---

## 🔮 Future Improvements

* Add collaborative filtering
* Use deep learning embeddings (BERT / Sentence Transformers)
* Deploy on cloud (AWS / GCP)
* Improve UI/UX

---

## 👨‍💻 Author

Akshat Gupta

---
