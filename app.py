import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("CARS.csv")
    return df

df = load_data()

# App Title
st.title("Car Brand Horsepower Explorer")

# Display top rows
st.subheader("Sample Data")
st.dataframe(df.head(5))

# Show unique car brands
brands = df["Make"].unique()
selected_brand = st.selectbox("Select a Car Brand", sorted(brands))

# Filter data
filtered_df = df[df.Make == selected_brand]

# Plot
if not filtered_df.empty:
    st.subheader(f"Horsepower of {selected_brand} Models")
    plt.figure(figsize=(10, 5))
    sb.barplot(x=filtered_df.Model, y=filtered_df.Horsepower)
    plt.xticks(rotation=90)
    st.pyplot(plt)
else:
    st.warning("No data available for the selected brand.")
