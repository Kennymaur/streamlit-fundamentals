import streamlit as st

st.write(
"""#My Interface
 This is my interface using Streamlit.
"""
)

sepal_height = st.number_input("Enter sepal height")
sepal_width = st.number_input("Enter sepal width")

petal_height = st.number_input("Enter petal height")
petal_width = st.number_input("Enter petal width")


if st.button("Predict"):
    st.text(f"The iris has been classified as : '{''}' .")