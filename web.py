import streamlit as st
import functions

import os
print("Current working directory:", os.getcwd())

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Labell", placeholder="Add new todo...")

