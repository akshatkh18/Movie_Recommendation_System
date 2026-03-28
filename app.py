import streamlit as st
import pandas as pd
import pickle

movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("similarity.pkl", "rb"))
poster_dict = pickle.load(open("poster_dict1.pkl", "rb"))

def recommend(movie):
    matched = movies[movies["title"].str.strip().str.lower() == movie.strip().lower()]

    if matched.empty:
        return [], []

    movie_index = matched.index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    names = []
    posters = []

    for i in movies_list:
        idx = i[0]
        movie_row = movies.iloc[idx]

        names.append(movie_row.title)
        poster = poster_dict[idx]

        if isinstance(poster, (list, tuple)) and len(poster) > 0:
            poster = poster[0]
        elif hasattr(poster, "shape"):  # numpy array
            poster = poster.item() if poster.size == 1 else None

        posters.append(poster)


    return names, posters

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    "Select a movie",
    ["Select a movie"] + movies["title"].tolist(),
    label_visibility="collapsed"
)

if st.button("Recommend"):
    if selected_movie_name == "Select a movie":
        st.warning("Please select a movie first")
    else:
        names, posters = recommend(selected_movie_name)

        cols = st.columns(5)
        for col, name, poster in zip(cols, names, posters):
            with col:
                st.subheader(name)
                if isinstance(poster, str) and poster.strip():
                    st.image(poster)
                else:
                    st.write("Poster unavailable")
