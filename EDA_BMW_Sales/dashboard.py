import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")
st.title("BMW Sales Dashboard 2010-2024")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("/Users/millicentomondi/Documents/AI_Saturdays_Exercises/EDA_BMW_Sales/BMW_sales.csv")

df = load_data()

# --- Summary Section ---
total_sales = df['Sales_Volume'].sum()
top_model = df.groupby('Model')['Sales_Volume'].sum().idxmax()
top_model_sales = df.groupby('Model')['Sales_Volume'].sum().max()

# Determine thresholds for sales classification
low_max = df[df['Sales_Classification'] == 'Low']['Sales_Volume'].max()
high_min = df[df['Sales_Classification'] == 'High']['Sales_Volume'].min()

st.markdown(f"**Total Sales Volume:** {total_sales:,} USD")
st.markdown(f"**Top Model Sold:** {top_model} ({top_model_sales:,} units)")
st.markdown(f"**Sales Volume Classification:** Low ≤ {low_max:,}, High ≥ {high_min:,}")

# --- Filters ---
st.sidebar.header("Filters")
year_range = st.sidebar.slider("Year Range", int(df['Year'].min()), int(df['Year'].max()), (2010, 2024))
region = st.sidebar.multiselect("Region", options=df['Region'].unique(), default=list(df['Region'].unique()))
model = st.sidebar.multiselect("Model", options=df['Model'].unique(), default=list(df['Model'].unique()))
transmission = st.sidebar.multiselect("Transmission", options=df['Transmission'].unique(), default=list(df['Transmission'].unique()))
fuel_type = st.sidebar.multiselect("Fuel Type", options=df['Fuel_Type'].unique(), default=list(df['Fuel_Type'].unique()))

filtered_df = df[
    (df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1]) &
    (df['Region'].isin(region)) &
    (df['Model'].isin(model)) &
    (df['Transmission'].isin(transmission)) &
    (df['Fuel_Type'].isin(fuel_type))
]

st.write("### Sample Data", filtered_df.head())

# --- Tabs Layout ---
tab1, tab2, tab3 = st.tabs(["Overview", "Engine Analysis", "Sales Classification"])

with tab1:
    st.subheader("Sales Over Time")
    fig, ax = plt.subplots(figsize=(7, 3))
    sns.lineplot(x='Year', y='Sales_Volume', data=filtered_df, ax=ax)
    st.pyplot(fig)

    st.subheader("Price by Year")
    fig, ax = plt.subplots(figsize=(7, 3))
    sns.lineplot(x='Year', y='Price_USD', data=filtered_df, ax=ax)
    st.pyplot(fig)

    st.subheader("Sales by Model")
    fig, ax = plt.subplots(figsize=(8, 3))
    sns.barplot(x='Model', y='Sales_Volume', data=filtered_df, estimator=sum, errorbar=None, ax=ax)
    plt.xticks(rotation=90)
    st.pyplot(fig)

    st.subheader("Sales by Region")
    fig, ax = plt.subplots(figsize=(7, 3))
    sns.barplot(x='Region', y='Sales_Volume', data=filtered_df, estimator=sum, errorbar=None, ax=ax)
    st.pyplot(fig)

    st.subheader("Sales by Transmission")
    fig, ax = plt.subplots(figsize=(7, 3))
    sns.barplot(x='Transmission', y='Sales_Volume', data=filtered_df, estimator=sum, errorbar=None, ax=ax)
    st.pyplot(fig)

    st.subheader("Sales by Fuel Type")
    fig, ax = plt.subplots(figsize=(7, 3))
    sns.barplot(x='Fuel_Type', y='Sales_Volume', data=filtered_df, estimator=sum, errorbar=None, ax=ax)
    st.pyplot(fig)

    st.subheader("Sales by Color")
    fig, ax = plt.subplots(figsize=(7, 3))
    sns.barplot(x='Color', y='Sales_Volume', data=filtered_df, estimator=sum, errorbar=None, ax=ax)
    st.pyplot(fig)

    st.subheader("Average Price by Color")
    fig, ax = plt.subplots(figsize=(7, 3))
    sns.barplot(x='Color', y='Price_USD', data=filtered_df, estimator='mean', errorbar=None, ax=ax)
    st.pyplot(fig)

with tab2:

    st.subheader("Engine Size by Model")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='Model', y='Engine_Size_L', data=filtered_df, estimator=sum, errorbar=None, ax=ax)
    ax.set_title('Engine Size by Model')
    ax.set_xlabel('Model')
    ax.set_ylabel('Engine Size (L)')
    st.pyplot(fig)

    st.subheader("Price by Engine Size")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='Engine_Size_L', y='Price_USD', data=filtered_df, estimator=sum, errorbar=None, ax=ax)
    ax.set_title('Price by Engine Size')
    ax.set_xlabel('Engine Size (L)')
    ax.set_ylabel('Price')
    st.pyplot(fig)

    st.subheader("Mileage by Engine Size")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='Engine_Size_L', y='Mileage_KM', data=filtered_df, estimator=sum, errorbar=None, ax=ax)
    ax.set_title('Mileage by Engine Size')
    ax.set_xlabel('Engine Size (L)')
    ax.set_ylabel('Mileage (KM)')
    st.pyplot(fig)

with tab3:

    st.subheader("Sales Classification by sales volume")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='Sales_Classification', y='Sales_Volume', data=filtered_df, estimator=sum, errorbar=None, ax=ax)
    ax.set_title('Sales Volume by Salles classification')
    ax.set_xlabel('Sales Classification')
    ax.set_ylabel('Sales Volume')
    st.pyplot(fig)

    st.subheader("Number of High and Low Sales per Fuel Type")
    sales_counts = filtered_df.groupby(['Fuel_Type', 'Sales_Classification']).size().unstack(fill_value=0)
    fig, ax = plt.subplots(figsize=(10, 6))
    sales_counts.plot(kind='bar', ax=ax)
    ax.set_title('Number of High and Low Sales per Fuel Type')
    ax.set_xlabel('Fuel Type')
    ax.set_ylabel('Count')
    plt.xticks(rotation=45)
    ax.legend(title='Sales Classification')
    plt.tight_layout()
    st.pyplot(fig)

    st.subheader("Number of High and Low Sales per Region")
    sales_counts = filtered_df.groupby(['Region', 'Sales_Classification']).size().unstack(fill_value=0)
    fig, ax = plt.subplots(figsize=(10, 6))
    sales_counts.plot(kind='bar', ax=ax)
    ax.set_title('Number of High and Low Sales per Region')
    ax.set_xlabel('Region')
    ax.set_ylabel('Count')
    plt.xticks(rotation=45)
    ax.legend(title='Sales Classification')
    plt.tight_layout()
    st.pyplot(fig)

    st.subheader("Number of High and Low Sales per Transmission")
    sales_counts = filtered_df.groupby(['Transmission', 'Sales_Classification']).size().unstack(fill_value=0)
    fig, ax = plt.subplots(figsize=(10, 6))
    sales_counts.plot(kind='bar', ax=ax)
    ax.set_title('Number of High and Low Sales per Transmission')
    ax.set_xlabel('Transmission')
    ax.set_ylabel('Count')
    plt.xticks(rotation=45)
    ax.legend(title='Sales Classification')
    plt.tight_layout()
    st.pyplot(fig)

    st.subheader("Number of High and Low Sales per year")
    sales_counts = filtered_df.groupby(['Year', 'Sales_Classification']).size().unstack(fill_value=0)
    fig, ax = plt.subplots(figsize=(10, 6))
    sales_counts.plot(kind='bar', ax=ax)
    ax.set_title('Number of High and Low Sales per Year')
    ax.set_xlabel('Year')
    ax.set_ylabel('Count')
    plt.xticks(rotation=45)
    ax.legend(title='Sales Classification')
    plt.tight_layout()
    st.pyplot(fig)

