import streamlit as st
import pandas as pd
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sales_df = pd.read_csv(
    os.path.join(BASE_DIR, "data", "processed", "cleaned_retail_data.csv")
)

forecast_df = pd.read_csv(
    os.path.join(BASE_DIR, "data", "processed", "forecast_data.csv")
)

rfm_df = pd.read_csv(
    os.path.join(BASE_DIR, "data", "processed", "rfm_customer_segments.csv")
)

inventory_df = pd.read_csv(
    os.path.join(BASE_DIR, "data", "processed", "inventory_data.csv")
)

st.title("NeuralRetail AI Dashboard")

page = st.sidebar.selectbox(
    "Select Dashboard",
    [
        "Executive Overview",
        "Sales Dashboard",
        "Forecast Dashboard",
        "Customer Dashboard",
        "Inventory Dashboard"
    ]
)

if page == "Executive Overview":

    st.header("Executive Overview")

    total_sales = sales_df["TotalSales"].sum()
    total_customers = sales_df["Customer ID"].nunique()
    total_orders = sales_df["Invoice"].nunique()
    avg_order_value = total_sales / total_orders

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Sales", f"${total_sales:,.0f}")
    col2.metric("Customers", total_customers)
    col3.metric("Orders", total_orders)
    col4.metric("Avg Order Value", f"${avg_order_value:,.2f}")



elif page == "Sales Dashboard":

    st.header("Sales Dashboard")

    monthly_sales = sales_df.groupby(
        "Month"
    )["TotalSales"].sum()

    st.subheader("Monthly Sales Trend")
    st.line_chart(monthly_sales)

    country_sales = sales_df.groupby(
        "Country"
    )["TotalSales"].sum().sort_values(
        ascending=False
    ).head(10)

    st.subheader("Top 10 Countries by Sales")
    st.bar_chart(country_sales)



elif page == "Forecast Dashboard":

    st.header("Forecast Dashboard")

    st.subheader("Actual vs Predicted Sales")

    forecast_chart = forecast_df[
        ["Sales", "PredictedSales"]
    ]

    st.line_chart(forecast_chart)



elif page == "Customer Dashboard":

    st.header("Customer Dashboard")

    st.subheader("RFM Score Distribution")

    rfm_counts = rfm_df[
        "RFM_Score"
    ].value_counts()

    st.bar_chart(rfm_counts)

    st.subheader("Top 10 Customers")

    top_customers = rfm_df.sort_values(
        "Monetary",
        ascending=False
    ).head(10)

    st.dataframe(top_customers)



elif page == "Inventory Dashboard":

    st.header("Inventory Dashboard")

    st.subheader("Top Products by Revenue")

    top_products = inventory_df.sort_values(
        "TotalRevenue",
        ascending=False
    ).head(10)

    chart_data = top_products.set_index(
        "Product"
    )["TotalRevenue"]

    st.bar_chart(chart_data)

    st.subheader("Low Stock Products")

    low_stock = inventory_df[
        inventory_df["LowStockAlert"] == 1
    ]

    st.dataframe(low_stock)