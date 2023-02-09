import requests
import streamlit as st

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

def get_demand():
    return requests.get(
        "http://127.0.0.1:8000/predict/demand"
    ).json()

def get_churn():
    return requests.get(
        "http://127.0.0.1:8000/predict/churn"
    ).json()
    
st.title("NeuralRetail AI Dashboard")


sales_df = pd.read_csv(
    "../data/processed/cleaned_retail_data.csv"
)

forecast_df = pd.read_csv(
    "../data/processed/forecast_data.csv"
)


page = st.sidebar.selectbox(

    "Select Dashboard",

    [
        "Sales Dashboard",
        "Forecast Dashboard"
    ]

)


if page == "Sales Dashboard":

    st.header("Sales Dashboard")

    total_sales = sales_df["TotalSales"].sum()

    st.metric(
        "Total Sales",
        f"${total_sales:,.2f}"
    )

    monthly_sales = sales_df.groupby(
        "Month"
    )["TotalSales"].sum()

    fig, ax = plt.subplots(figsize=(10,5))

    monthly_sales.plot(ax=ax)

    plt.title("Monthly Sales")

    st.pyplot(fig)


elif page == "Forecast Dashboard":

    st.header("Forecast Dashboard")

    fig, ax = plt.subplots(figsize=(12,5))

    ax.plot(
        forecast_df["Date"],
        forecast_df["Sales"],
        label="Actual Sales"
    )

    ax.plot(
        forecast_df["Date"],
        forecast_df["PredictedSales"],
        label="Predicted Sales"
    )

    plt.legend()

    st.pyplot(fig)