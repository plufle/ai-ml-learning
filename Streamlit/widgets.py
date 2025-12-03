import streamlit as st
import pandas as pd


st.title("Widgets")

anme = st.text_input("Name")
st.write("Hello", anme)

age = st.slider("Age", 0, 100)
st.write("Age", age)

option = st.selectbox("Select", ["Option 1", "Option 2", "Option 3"])
st.write("Option", option)


data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file=st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)