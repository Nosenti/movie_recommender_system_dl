import streamlit as st
import numpy as np
import pandas as pd
# load the model
from keras.models import load_model
model = load_model( 'model.h5' )

column_names = ['user_id','item_id','rating','timestamp']
df = pd.read_csv('u.data',sep='\t',names=column_names)

movie_titles = pd.read_csv('Movie_Id_Titles')
#open movies list
df = pd.merge(df,movie_titles,on='item_id')

st.title('Demo')

f = open("demofile.txt", "r")
unique_movies = list(map(int, f.read().split(',')))

# st.write(unique_movies)


user_id = st.number_input('user_id', 0, len(unique_movies), 0)


st.write(user_id)

user_arr = np.array([user_id for i in range(len(unique_movies))])

st.write(type(user_arr))

# predict = model.predict(X_test_array)
movie_arr = np.array(unique_movies)
predict  = model.predict([user_arr, movie_arr])
if st.button("Predict"):
  st.write(predict)
  st.dataframe(df)
  predict = predict.reshape(-1)
  predict_id = (-predict).argsort()[0:5]
  predict_id
  st.write(df.iloc[predict_id].title)
