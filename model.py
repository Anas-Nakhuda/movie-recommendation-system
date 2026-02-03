import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def load_data():
    ratings = pd.read_csv("data/ratings.csv")
    movies = pd.read_csv("data/movies.csv")

    # Create movie-user matrix
    matrix = ratings.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)

    similarity = cosine_similarity(matrix)

    return similarity, ratings, movies


def recommend_movies(user_id, similarity, ratings, movies):
    scores = list(enumerate(similarity[user_id]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    similar_users = [i[0] for i in scores[1:6]]

    # Get movies watched by similar users
    rec_movies = ratings[ratings['userId'].isin(similar_users)]

    movie_ids = rec_movies['movieId'].unique()[:5]

    titles = movies[movies['movieId'].isin(movie_ids)]['title']

    return titles.tolist()
