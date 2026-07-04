import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Shopping Dashboard", layout="wide")

# -------------------------------------------------
# 1. LOAD DATA
# -------------------------------------------------
df = pd.read_csv("customer_shopping_data.csv")

# add the two new columns
df["invoice_date"] = pd.to_datetime(df["invoice_date"], dayfirst=True)
df["total"] = df["quantity"] * df["price"]
df["month"] = df["invoice_date"].dt.strftime("%b")

# -------------------------------------------------
# 2. SIDEBAR FILTERS
# -------------------------------------------------
st.sidebar.header("Filters")

category_filter = st.sidebar.multiselect(
    "Category", df["category"].unique(), default=df["category"].unique()
)
month_filter = st.sidebar.multiselect(
    "Month", df["month"].unique(), default=df["month"].unique()
)
gender_filter = st.sidebar.multiselect(
    "Gender", df["gender"].unique(), default=df["gender"].unique()
)
payment_filter = st.sidebar.multiselect(
    "Payment Method", df["payment_method"].unique(), default=df["payment_method"].unique()
)

# apply filters
df = df[
    df["category"].isin(category_filter)
    & df["month"].isin(month_filter)
    & df["gender"].isin(gender_filter)
    & df["payment_method"].isin(payment_filter)
]

# -------------------------------------------------
# 3. TITLE
# -------------------------------------------------
st.title("🛍️ Customer Shopping Dashboard")

# -------------------------------------------------
# 4. KPI CARDS
# -------------------------------------------------
revenue = df["total"].sum()
orders = df["invoice_no"].nunique()
aov = revenue / orders if orders else 0

col1, col2, col3 = st.columns(3)
col1.metric("Revenue", f"${revenue:,.0f}")
col2.metric("Orders", f"{orders:,}")
col3.metric("Avg Order Value", f"${aov:,.2f}")

st.markdown("---")

# -------------------------------------------------
# 5. MONTHLY SALES TREND
# -------------------------------------------------
st.subheader("Monthly Sales Trend")

month_order = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
monthly_sales = df.groupby("month")["total"].sum().reindex(month_order).dropna()

fig1 = px.line(monthly_sales, x=monthly_sales.index, y=monthly_sales.values, markers=True)
fig1.update_layout(xaxis_title="Month", yaxis_title="Revenue")
st.plotly_chart(fig1, use_container_width=True)

# -------------------------------------------------
# 6. SALES BY CATEGORY & GENDER
# -------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Sales by Category")
    category_sales = df.groupby("category")["total"].sum().sort_values(ascending=False)
    fig2 = px.bar(category_sales, x=category_sales.index, y=category_sales.values)
    fig2.update_layout(xaxis_title="Category", yaxis_title="Revenue")
    st.plotly_chart(fig2, use_container_width=True)

with col2:
    st.subheader("Sales by Gender")
    gender_sales = df.groupby("gender")["total"].sum()
    fig3 = px.pie(gender_sales, names=gender_sales.index, values=gender_sales.values)
    st.plotly_chart(fig3, use_container_width=True)

# -------------------------------------------------
# 7. PAYMENT METHOD & AGE GROUP
# -------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Payment Method Distribution")
    payment_counts = df["payment_method"].value_counts()
    fig4 = px.bar(payment_counts, x=payment_counts.index, y=payment_counts.values)
    fig4.update_layout(xaxis_title="Payment Method", yaxis_title="Number of Orders")
    st.plotly_chart(fig4, use_container_width=True)

with col2:
    st.subheader("Age Group Analysis")
    bins = [0, 18, 25, 35, 45, 55, 65, 100]
    labels = ["<18", "18-25", "26-35", "36-45", "46-55", "56-65", "65+"]
    df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels)
    age_sales = df.groupby("age_group", observed=True)["total"].sum()
    fig5 = px.bar(age_sales, x=age_sales.index, y=age_sales.values)
    fig5.update_layout(xaxis_title="Age Group", yaxis_title="Revenue")
    st.plotly_chart(fig5, use_container_width=True)

# -------------------------------------------------
# 8. KEY INSIGHTS
# -------------------------------------------------
st.markdown("---")
st.subheader("Key Insights")

top_category = category_sales.index[0]
top_month = monthly_sales.idxmax()
top_payment = payment_counts.index[0]

st.write(f"- Top category: **{top_category}**")
st.write(f"- Best month: **{top_month}**")
st.write(f"- Most used payment method: **{top_payment}**")

# -------------------------------------------------
# 9. RAW DATA TABLE
# -------------------------------------------------
with st.expander("View Data"):
    st.dataframe(df)
