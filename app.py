import streamlit as st
import numpy as np
# load the model
from keras.models import load_model
model = load_model( 'model.h5' )

#open and read the file after the appending:
f = open("demofile.txt", "r")
unique_movies = list(map(int, f.read().split(',')))

st.write(unique_movies)
st.title('Demo')

user_id = st.number_input('user_id', 0, len(unique_movies), 0)


st.write(user_id)

user_arr = np.array([5 for i in range(len(unique_movies))])

st.write(user_arr)

# predict = model.predict(X_test_array)
predict  = model.predict([user_arr, unique_movies])
st.write(predict)
