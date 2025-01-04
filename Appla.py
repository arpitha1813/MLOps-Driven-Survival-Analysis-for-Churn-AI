import streamlit as st
import pandas as pd
import joblib
from lifelines import CoxPHFitter
import numpy as np

# Load models and preprocessors
@st.cache_resource
def load_models():
    scaler = joblib.load('scaler.pkl')
    pca = joblib.load('pca_model.pkl')
    cox_model = joblib.load('cox_model.pkl')
    best_ensemble_model = joblib.load('best_ensemble_model.pkl')
    return scaler, pca, cox_model, best_ensemble_model

scaler, pca, cox_model, best_ensemble_model = load_models()

# App title
st.title("Telco Customer Churn Prediction & Survival Analysis")

# Sidebar for user input
st.sidebar.header("Enter Customer Details")

# Collect customer inputs
tenure_months = st.sidebar.slider("Tenure (Months)", min_value=0, max_value=72, value=12)
churn_score = st.sidebar.slider("Age", min_value=0, max_value=100, value=50)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
senior_citizen = st.sidebar.selectbox("Senior Citizen", ["Yes", "No"])
partner = st.sidebar.selectbox("Partner", ["Yes", "No"])
dependents = st.sidebar.selectbox("Dependents", ["Yes", "No"])
multiple_lines = st.sidebar.selectbox("Multiple Lines", ["Yes", "No"])
internet_service = st.sidebar.selectbox("Internet Service", ["Yes", "No"])
online_security = st.sidebar.selectbox("Online Security", ["Yes", "No"])
online_backup = st.sidebar.selectbox("Online Backup", ["Yes", "No"])
device_protection = st.sidebar.selectbox("Device Protection", ["Yes", "No"])
tech_support = st.sidebar.selectbox("Tech Support", ["Yes", "No"])
streaming_tv = st.sidebar.selectbox("Streaming TV", ["Yes", "No"])
streaming_movies = st.sidebar.selectbox("Streaming Movies", ["Yes", "No"])
paperless_billing = st.sidebar.selectbox("Paperless Billing", ["Yes", "No"])

# Feature engineering for user input
input_data = pd.DataFrame({
    'Tenure Months': [tenure_months],
    'Churn Score': [churn_score],
    'Gender_Male': [1 if gender == "Male" else 0],
    'Senior Citizen_Yes': [1 if senior_citizen == "Yes" else 0],
    'Partner_Yes': [1 if partner == "Yes" else 0],
    'Dependents_Yes': [1 if dependents == "Yes" else 0],
    'Multiple Lines_Yes': [1 if multiple_lines == "Yes" else 0],
    'Internet Service_Yes': [1 if internet_service == "Yes" else 0],
    'Online Security_Yes': [1 if online_security == "Yes" else 0],
    'Online Backup_Yes': [1 if online_backup == "Yes" else 0],
    'Device Protection_Yes': [1 if device_protection == "Yes" else 0],
    'Tech Support_Yes': [1 if tech_support == "Yes" else 0],
    'Streaming TV_Yes': [1 if streaming_tv == "Yes" else 0],
    'Streaming Movies_Yes': [1 if streaming_movies == "Yes" else 0],
    'Paperless Billing_Yes': [1 if paperless_billing == "Yes" else 0],
})

# Display user input
st.write("### Customer Input:")
#st.write(input_data)

# Button for triggering predictions
if st.button('Predict Churn, Survival Analysis, and Customer Segment'):
    try:
        # Scale features
        input_data_scaled = scaler.transform(input_data[['Churn Score']])
        input_data[['Churn Score']] = input_data_scaled

        # PCA Transformation
        input_data_pca = pca.transform(input_data)

        # Churn Prediction using Ensemble Model
        churn_prediction = best_ensemble_model.predict(input_data_pca)
        churn_probability = best_ensemble_model.predict_proba(input_data_pca)[:, 1]  # Probability of churn
        #  time=survival_prediction.index[((survival_prediction.index - time_point).abs()).argmin()]

       # Make sure to predict the survival function before using it
        survival_prediction = cox_model.predict_survival_function(input_data)

        # Set the target time point for which you want to predict survival
        time_point = 100  # Example time point, adjust this as needed

# Convert the index to a numpy array to calculate the absolute difference
        time_index = survival_prediction.index.to_numpy()

# Find the closest available time point
        nearest_time_point = time_index[np.abs(time_index - time_point).argmin()]

# Get survival probability for the nearest time point
        survival_predicted_value = survival_prediction.loc[nearest_time_point].values[0]

        # Define customer segment based on survival probability
        if survival_predicted_value < 0.8:
            customer_segment_label = "High Risk"
        else:
            customer_segment_label = "Low Risk"

        # Display results for churn prediction
        if churn_prediction == 1:
            st.markdown(f"<h2 style='color:red;'>Churn Prediction: **YES**</h2>", unsafe_allow_html=True)
            st.markdown(f"Probability of Churn: {churn_probability[0] * 100:.2f}%", unsafe_allow_html=True)
        else:
            st.markdown(f"<h2 style='color:green;'>Churn Prediction: **NO**</h2>", unsafe_allow_html=True)
            st.markdown(f"Probability of Not Churning: {(1 - churn_probability[0]) * 100:.2f}%", unsafe_allow_html=True)

        # Display results for survival analysis
        st.markdown(f"Survival Probability : {survival_predicted_value:.2f}")

        # Display customer segment
        st.markdown(f"<h2 style='color:blue;'>Customer Segment: **{customer_segment_label}**</h2>", unsafe_allow_html=True)

    except ValueError as e:
        st.error(f"Error: {str(e)}")
else:
    st.write("Please fill out all the inputs and press 'Predict Churn, Survival Analysis, and Customer Segment'.")
