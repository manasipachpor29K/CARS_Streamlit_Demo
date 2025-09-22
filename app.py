import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from PIL import Image

# Load CSV locally
df = pd.read_csv("CARS.csv")  # Make sure this file is in the same folder

# Set background image (light transparent car image)
page_bg_img = """
<style>
.stApp {
background-image: url("https://i.ibb.co/YZB7xjX/light-car-background.jpg");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

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

# Select Plot Type
plot_type = st.sidebar.radio("Select Plot Type", ["Bar Plot", "Line Plot", "Scatter Plot", "Pie Chart"])

# Filter data for the selected brand
brand_df = df[df['Make'] == selected_brand]

# Section Title
st.subheader(f"🚗 Visualization for {selected_brand}")
st.write("Select the type of chart from the sidebar and choose a color palette.")

if not brand_df.empty:
    plt.figure(figsize=(12, 6))

    if plot_type == "Bar Plot":
        sb.barplot(
            y='Model',
            x='Horsepower',
            data=brand_df,
            palette=selected_palette
        )
        plt.xlabel("Horsepower")
        plt.ylabel("Model")
        plt.title(f"Horsepower of {selected_brand} Models", fontsize=16)

    elif plot_type == "Line Plot":
        sb.lineplot(
            x='Model',
            y='Horsepower',
            data=brand_df,
            marker='o',
            color='steelblue'
        )
        plt.xticks(rotation=45, ha='right')
        plt.xlabel("Model")
        plt.ylabel("Horsepower")
        plt.title(f"Horsepower of {selected_brand} Models (Line Plot)", fontsize=16)

    elif plot_type == "Scatter Plot":
        sb.scatterplot(
            x='Model',
            y='Horsepower',
            size='Horsepower',
            hue='Horsepower',
            palette=selected_palette,
            data=brand_df,
            sizes=(50, 300),
            legend=False
        )
        plt.xticks(rotation=45, ha='right')
        plt.xlabel("Model")
        plt.ylabel("Horsepower")
        plt.title(f"Horsepower Scatter of {selected_brand} Models", fontsize=16)

    elif plot_type == "Pie Chart":
        plt.pie(
            brand_df['Horsepower'],
            labels=brand_df['Model'],
            autopct='%1.1f%%',
            colors=sb.color_palette(selected_palette,
