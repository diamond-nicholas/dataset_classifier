import streamlit as st

st.title('Welcome')
st.write("""
### Explore different classifier
which one is the best
""")

st.selectbox('Select Dataset', ("Iris", "Breast Cancer", "Wine Dataset"))