import streamlit as st
from sklearn import datasets
import numpy as np

st.title('Welcome')
st.write("""
### Explore different classifier
which one is the best
""")

dataset_name = st.sidebar.selectbox('Select Dataset', ("Iris", "Breast Cancer", "Wine Dataset"))
classifier_name = st.sidebar.selectbox('Select Classifier', ("KNN", "SVM", "Random Forest"))

def get_dataset(dataset_name):
    if dataset_name == 'Iris': 
        data = datasets.load_iris()
    elif dataset_name == 'Breast Cancer':
        data = datasets.load_breast_cancer()
    else:
        data = datasets.load_wine()
    X = data.data
    y = data.target
    return X, y
X, y = get_dataset(dataset_name)

st.write('Shape of the dataset', X.shape)
st.write('Number of classes', len(np.unique(y)))


