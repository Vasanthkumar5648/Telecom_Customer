import streamlit as st
from joblib import load

# Load the trained Random Forest model
model = load('random_forest_model.joblib')

#creating a background

st.markdown(
    """
    <style>
        html, body, .stApp {
            font-family: 'Arial', sans-serif; /* Change font here */
            background-color: #FFFFFF;
        }

        .title-box {
            font-family: 'Helvetica', sans-serif;
            font-size: 28px;
            font-weight: bold;
            text-align: center;
            color: black;
        }

        .prediction-box {
            background-color:#D3D3D3;
            font-family: 'Courier New', monospace;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            color: black;
        }

        .custom-text {
            font-family: 'Verdana', sans-serif;
            font-size: 16px;
            color: black;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a Streamlit app
st.title("📊 Customer Churn Prediction App")
# Input fields for feature values on the main screen
st.sidebar.header("Enter Customer Information")
tenure = st.sidebar.selectbox("Tenure (in months)", list(range(0, 110, 10)))
internet_service = st.sidebar.selectbox("Internet Service", ('DSL', 'Fiber optic', 'No'))
contract = st.sidebar.selectbox("Contract", ('Month-to-month', 'One year', 'Two year'))
monthly_charges = st.sidebar.selectbox("Monthly Charges", list(range(0, 210, 10)))
total_charges = st.sidebar.selectbox("Total Charges", list(range(0, 10100, 10)))

# Predict Button
if st.sidebar.button("Predict Churn"):
    st.subheader("🔍 Selected Input Values")
    st.write(f"**Tenure:** {tenure} months")
    st.write(f"**Internet Service:** {internet_service}")
    st.write(f"**Contract:** {contract}")
    st.write(f"**Monthly Charges:** ${monthly_charges}")
    st.write(f"**Total Charges:** ${total_charges}")

# Map input values to numeric using the label mapping
label_mapping = {
    'DSL': 0,
    'Fiber optic': 1,
    'No': 2,
    'Month-to-month': 0,
    'One year': 1,
    'Two year': 2,
}
internet_service = label_mapping[internet_service]
contract = label_mapping[contract]

# Make a prediction using the model
prediction = model.predict([[tenure, internet_service, contract, monthly_charges, total_charges]])

# Display the prediction result on the main screen
st.header("Prediction Result")
if prediction[0] == 0:
    st.markdown('<div class="prediction-box" style="color: Blue;">✅ This customer is likely to stay.</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="prediction-box" style="color: Red;">⚠️ This customer is likely to churn.</div>', unsafe_allow_html=True)
