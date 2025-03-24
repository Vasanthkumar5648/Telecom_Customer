import streamlit as st
import joblib
import os

# Load model safely
MODEL_PATH = "random_forest_model.joblib"

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    st.error("❌ Model file not found. Upload 'random_forest_model.joblib'.")

st.title("📊 Customer Churn Prediction App")

st.sidebar.header("Enter Customer Information")
tenure = st.sidebar.number_input("Tenure (months)", min_value=0, max_value=100, step=1)
internet_service = st.sidebar.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])
contract = st.sidebar.selectbox("Contract", ['Month-to-month', 'One year', 'Two year'])
monthly_charges = st.sidebar.number_input("Monthly Charges ($)", min_value=0, max_value=200, step=5)
total_charges = st.sidebar.number_input("Total Charges ($)", min_value=0, max_value=10000, step=50)

if st.sidebar.button("Predict Churn"):
    label_mapping = {'DSL': 0, 'Fiber optic': 1, 'No': 2, 'Month-to-month': 0, 'One year': 1, 'Two year': 2}
    internet_service = label_mapping[internet_service]
    contract = label_mapping[contract]

    try:
        prediction = model.predict([[tenure, internet_service, contract, monthly_charges, total_charges]])
        st.header("Prediction Result")
        if prediction[0] == 0:
            st.success("✅ This customer is likely to stay.")
        else:
            st.warning("⚠️ This customer is likely to churn.")
    except Exception as e:
        st.error(f"Error: {e}")
