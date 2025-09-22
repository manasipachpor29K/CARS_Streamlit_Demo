import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Load CSV from GitHub
csv_url = "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/CARS.csv"
df = pd.read_csv("Cars.csv")

# Sidebar - user inputs
st.sidebar.header("Filter Options")
brands = df['Make'].unique()
selected_brand = st.sidebar.selectbox("Select Car Brand", brands)

color_palettes = ["viridis", "plasma", "magma", "cividis", "coolwarm", "Set2", "pastel"]
selected_palette = st.sidebar.selectbox("Select Color Palette", color_palettes)

# Filter data by brand
filtered_df = df[df['Make'] == selected_brand]

# Title
st.title(f"🚗 Horsepower of {selected_brand} Cars")
st.write("Interactive bar plot with selectable color palettes for creativity.")

# Plot
if not filtered_df.empty:
    plt.figure(figsize=(12, 6))
    sb.barplot(
        x='Model',
        y='Horsepower',
        data=filtered_df,
        palette=selected_palette
    )
    plt.xticks(rotation=45, ha='right')
    plt.ylabel("Horsepower")
    plt.xlabel("Model")
    plt.title(f"Horsepower of {selected_brand} Models", fontsize=16)
    st.pyplot(plt.gcf())
else:
    st.warning("⚠️ No data available for this brand.")
