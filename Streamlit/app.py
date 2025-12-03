import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello World")

st.write("This is a streamlit app")

df = pd.DataFrame(
    np.random.randn(100, 2),
    columns=["x", "y"]
)
st.write(df)

st.line_chart(df)

