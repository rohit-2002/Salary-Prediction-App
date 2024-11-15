import streamlit as st
import pickle
import numpy as np
import pandas as pd
import plotly.express as px

# Load the saved Linear Regression model
model = pickle.load(open('linear_regression_model.pkl', 'rb'))

# Custom CSS for better UI styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f7f9fc;
        color: #333333;
        font-family: Arial, sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px;
        border-radius: 5px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App title and description
st.title("📊 Salary Prediction App")
st.write("### Predict your salary based on years of experience using a machine learning model.")
st.markdown("This app utilizes a **Linear Regression Model** for making salary predictions.")

# Sidebar for user input
st.sidebar.header("Input Options")
years_experience = st.sidebar.number_input(
    "Enter Years of Experience:", min_value=0.0, max_value=50.0, value=1.0, step=0.5
)

# Option to upload a CSV file
st.sidebar.write("Alternatively, upload a CSV file with a `YearsExperience` column:")
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

# Single prediction for user input
if st.button("Predict Salary"):
    experience_input = np.array([[years_experience]])  # Reshape input for prediction
    prediction = model.predict(experience_input)
    st.success(f"💼 The predicted salary for {years_experience} years of experience is: **${prediction[0]:,.2f}**")

    # Visualizing the salary trend
    st.write("### Salary Trend Visualization")
    years = np.linspace(0, 50, 100).reshape(-1, 1)
    salaries = model.predict(years)
    fig = px.line(
        x=years.flatten(),
        y=salaries.flatten(),
        labels={"x": "Years of Experience", "y": "Predicted Salary"},
        title="Predicted Salary vs. Years of Experience",
    )
    st.plotly_chart(fig)

# Batch prediction for uploaded dataset
if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)

        if "YearsExperience" in data.columns:
            # Make predictions for the dataset
            data["Predicted Salary"] = model.predict(data[["YearsExperience"]])

            # Display predictions
            st.write("### Predictions for the Uploaded Dataset:")
            st.dataframe(data)

            # Option to download results
            csv = data.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Download Predictions as CSV",
                data=csv,
                file_name="predicted_salaries.csv",
                mime="text/csv",
            )

            # Visualizing data
            st.write("### Data Distribution and Comparison")
            if "ActualSalary" in data.columns:
                fig = px.bar(
                    data,
                    x="YearsExperience",
                    y=["ActualSalary", "Predicted Salary"],
                    barmode="group",
                    title="Actual vs. Predicted Salaries",
                )
                st.plotly_chart(fig)
            else:
                st.bar_chart(data.set_index("YearsExperience")["Predicted Salary"])
        else:
            st.error("The uploaded CSV must have a `YearsExperience` column.")

    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")

# Footer
st.markdown(
    """
    ---
    *Powered by [Streamlit](https://streamlit.io) and crafted with passion!*
    """
)
