import os

import requests
import streamlit as st

# gowa compose bnklm el api b esm el service mesh localhost
API_URL = os.environ["API_URL"] if "API_URL" in os.environ else "http://api:8000"

st.set_page_config(page_title="Iris Classifier")
st.title("Iris Classifier")
st.write("Enter the four flower measurements in centimetres to predict the iris species.")

with st.form("predict_form"):
    col1, col2 = st.columns(2)
    with col1:
        sepal_length = st.number_input("Sepal length (cm)", min_value=0.0, value=5.1, step=0.1)
        petal_length = st.number_input("Petal length (cm)", min_value=0.0, value=1.4, step=0.1)
    with col2:
        sepal_width = st.number_input("Sepal width (cm)", min_value=0.0, value=3.5, step=0.1)
        petal_width = st.number_input("Petal width (cm)", min_value=0.0, value=0.2, step=0.1)
    submitted = st.form_submit_button("Predict")


if submitted:
    # lazem nfs el tarteeb elly el api mstneeh
    payload = {"feature_array": [sepal_length, sepal_width, petal_length, petal_width]}

    try:
        response = requests.post(f"{API_URL}/predict", json=payload, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        st.error(f"Could not get a prediction from the API: {e}")
    else:
        prediction = response.json()["prediction"]
        st.success(f"Predicted species: **{prediction['class_name']}**")
