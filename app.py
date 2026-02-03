import streamlit as st
from model import load_data, recommend_movies

st.title("🎬 Movie Recommendation System")

similarity, ratings, movies = load_data()

user_id = st.number_input("Enter User ID", min_value=1, max_value=943)

if st.button("Recommend"):
    recommendations = recommend_movies(user_id, similarity, ratings, movies)

    st.subheader("Recommended Movies 🎥")

    for movie in recommendations:
        st.write("•", movie)
