import streamlit as st
import pickle
import pandas as pd

with open('gender_classification_model.pkl', 'rb') as file:
    model = pickle.load(file)


def predict_gender(features):
    prediction = model.predict([features])
    return "Male" if prediction[0] == 1 else "Female"

st.title("Gender Classification Model")

long_hair = st.number_input("Size of Long Hair:")
forehead_width_cm = st.number_input("Size of forehead_width_cm:")
forehead_height_cm = st.number_input("Size of forehead_height_cm:")
nose_wide = st.number_input("Size of nose_wide:")
nose_long = st.number_input("Size of nose_long:")
lips_thin = st.number_input("Size of lips_thin:")
distance_nose_to_lip_long = st.number_input("Size of distance_nose_to_lip_long:")


if(st.button("Predict Gender :")):
    features = [long_hair, forehead_width_cm, forehead_height_cm, nose_wide, nose_long, lips_thin, distance_nose_to_lip_long]
    prediction = predict_gender(features)
    st.write(f"The Predicted Gender is : {prediction}")
