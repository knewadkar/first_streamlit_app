import streamlit as st

st.title("Title : Hello StreamLit")

st.header('Breakfast Menu')
st.text(' Omega 3 & Blueberry Oatmeal')
st.text('Kale, Spinach & Rocket Smoothie')
st.text('Hard-Boiled Free-Range Egg')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#st.dataframe(my_fruit_list)
st.multiselect("Pick some fruits : ", list(my_fruit_list.index))
st.dataframe(my_fruit_list)
