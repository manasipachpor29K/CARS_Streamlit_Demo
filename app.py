import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Load CSV locally
df = pd.read_csv("CARS.csv")  # Make sure this file is in the same folder

# Sidebar filters
st.sidebar.header("Filter Options")

# Select Brand
brands = df['Make'].unique()
selected_brand = st.sidebar.selectbox("Select Car Brand", brands)

# Select Car Model
models = df[df['Make'] == selected_brand]['Model'].unique()
selected_model = st.sidebar.selectbox("Select Car Model", models)

# Color palette selection
color_palettes = ["viridis", "plasma", "magma", "cividis", "coolwarm", "Set2", "pastel"]
selected_palette = st.sidebar.selectbox("Select Color Palette", color_palettes)

# Filter data for plotting
brand_df = df[df['Make'] == selected_brand]

# Title
st.title(f"🚗 Horsepower Visualization for {selected_brand}")
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

# Show details of the selected car
st.subheader(f"📋 Details for {selected_model}")
car_details = df[(df['Make'] == selected_brand) & (df['Model'] == selected_model)]
st.dataframe(car_details.T)  # Transposed for better readability
