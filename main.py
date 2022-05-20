import streamlit as st

st.title('Welcome')
st.write("""
### Explore different classifier
which one is the best
""")

dataset_name = st.sidebar.selectbox('Select Dataset', ("Iris", "Breast Cancer", "Wine Dataset"))
classifier_name = st.sidebar.selectbox('Select Classifier', ("KNN", "SVM", "Random Forest"))
