import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('football_result_prediction.pkl', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title="Football Match Predictor", layout="centered")

# App title
st.title("⚽ Football Match Predictor")

# Team selection
teams = ["Team A", "Team B", "Team C", "Team D"]  # replace with your actual teams

home_team = st.selectbox("Select Home Team", teams)
away_team = st.selectbox("Select Away Team", teams)



if st.button("Predict"):
    # Prepare input for prediction
    # Replace this with your actual feature preprocessing
    input_df = pd.DataFrame({
        'home_team': [home_team],
        'away_team': [away_team],
        # Add other features here
    })
    
    # If your model needs encoding, do it here
    # Example: input_df = pd.get_dummies(input_df)

    # Prediction
    prediction = model.predict(input_df)
    st.success(f"Predicted Outcome: {prediction[0]}")
