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
    # st.write(y)
    return X, y
X, y = get_dataset(dataset_name)

st.write('Shape of the dataset', X.shape)
st.write('Number of classes', len(np.unique(y)))

def add_parameter_ui(clf_name):
    params = dict()
    if clf_name == 'KNN': 
        K = st.sidebar.slider('K', 1,15)
        params["k"] = K
    elif clf_name == "SVM":
        C = st.sidebar.slider("C", 0.01,10.0)
        params["C"] = C
    else:
        max_depth = st.sidebar.slider("max_depth", 2, 15)
        n_estimators = st.sidebar.slider("n_estimators", 1, 100)
        params["max_depth"] = max_depth
        params["n_estimators"] = n_estimators
        return params

add_parameter_ui(classifier_name)