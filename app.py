import streamlit as st
import pickle as pk

movies = pk.load(open("./dump/data.pkl","rb"))
similarity = pk.load(open("./dump/similarity.pkl","rb"))

st.title("Movie Recommender System")
movie_selected = st.selectbox("Movie",options=movies["title"].values)

def recommend(movie):
  movie_index = movies[movies["title"] == movie].index[0]
  distances = similarity[movie_index]
  movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
  res = []
  for i in movie_list:
    res.append(movies.iloc[i[0]].title)
  return res
def Recommend_Movie():
  result = recommend(movie_selected)
  for i in  result:
    st.write(i)

st.button("Recommend",on_click=Recommend_Movie)