import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster_omdb(movie_title):
    """Fetches the poster URL for a given movie title using OMDb API."""
    api_key = "7063f213"  # Replace with your OMDb API key
    base_url = "http://www.omdbapi.com/"
    params = {"apikey": api_key, "t": movie_title}
    response = requests.get(base_url, params=params)
    data = response.json()
    if "Poster" in data and data["Poster"] != "N/A":
        return data["Poster"]
    return None

def recommend(movie):
    """Recommends movies based on similarity and fetches their posters."""
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        movie_title = movies.iloc[i[0]].title
        recommended_movies.append(movie_title)
        recommended_posters.append(fetch_poster_omdb(movie_title))
    return recommended_movies, recommended_posters

# Load movie data and similarity matrix
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit app
st.title('Personlized Movie Recommendation System')

selected_movie_name = st.selectbox(
    'Please select a movie and 5 recommended movies will be shown as per your choice',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations, posters = recommend(selected_movie_name)
    for movie, poster in zip(recommendations, posters):
        if poster:
            st.image(poster, width=150)
        st.write(movie)
