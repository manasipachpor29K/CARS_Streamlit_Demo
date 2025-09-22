import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Load CSV locally
df = pd.read_csv("CARS.csv")  # Make sure this file is in the same folder

# Top colorful headline
st.markdown(
    """
    <h1 style='text-align: center; font-weight: bold; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
               -webkit-background-clip: text; color: transparent;'>
        Cars Data
    </h1>
    """,
    unsafe_allow_html=True
)

# Sidebar filters
st.sidebar.header("Filter Options")

# Select Brand
brands = df['Make'].unique()
selected_brand = st.sidebar.selectbox("Select Car Brand", brands)

# Color palette selection
color_palettes = ["viridis", "plasma", "magma", "cividis", "coolwarm", "Set2", "pastel"]
selected_palette = st.sidebar.selectbox("Select Color Palette", color_palettes)

# Filter data for the selected brand
brand_df = df[df['Make'] == selected_brand]

# Section Title
st.subheader(f"🚗 Horsepower Visualization for {selected_brand}")
st.write("Explore horsepower of car models with a selectable color palette.")

# Plot horsepower bar chart
if not brand_df.empty:
    plt.figure(figsize=(12, 6))
    sb.barplot(
        x='Model',
        y='Horsepower',
        data=brand_df,
        palette=selected_palette
    )
    plt.xticks(rotation=45, ha='right')
    plt.ylabel("Horsepower")
    plt.xlabel("Model")
    plt.title(f"Horsepower of {selected_brand} Models", fontsize=16)
    st.pyplot(plt.gcf())
else:
    st.warning("⚠️ No data available for this brand.")

# Show all details for the selected brand
st.subheader(f"📋 All Details for {selected_brand}")
st.dataframe(brand_df)
