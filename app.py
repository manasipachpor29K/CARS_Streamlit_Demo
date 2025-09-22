import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="Car Horsepower Explorer", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("CARS.csv")
    return df

df = load_data()

# Title and subtitle
st.title("🚗 Car Horsepower Visualizer")
st.markdown("Use the sidebar to **filter data**, choose **color palettes**, and **select chart types** to explore horsepower across different car models and brands.")

# Sidebar filters
st.sidebar.header("🔧 Filters")

# Brand selection
brands = sorted(df["Make"].unique())
selected_brand = st.sidebar.selectbox("Select Car Brand", brands)

# Filter by brand
filtered_df = df[df["Make"] == selected_brand]

# Horsepower range filter
min_hp = int(filtered_df["Horsepower"].min())
max_hp = int(filtered_df["Horsepower"].max())
hp_range = st.sidebar.slider("Select Horsepower Range", min_value=min_hp, max_value=max_hp, value=(min_hp, max_hp))
filtered_df = filtered_df[(filtered_df["Horsepower"] >= hp_range[0]) & (filtered_df["Horsepower"] <= hp_range[1])]

# Model selection
models = sorted(filtered_df["Model"].unique())
selected_models = st.sidebar.multiselect("Select Models (optional)", models, default=models)
filtered_df = filtered_df[filtered_df["Model"].isin(selected_models)]

# Color palette
st.sidebar.markdown("---")
st.sidebar.subheader("🎨 Color & Chart")
color_palettes = [
    "viridis", "plasma", "inferno", "magma", "cividis",
    "coolwarm", "Spectral", "cubehelix", "Blues", "Greens", "Oranges", "Purples"
]
selected_palette = st.sidebar.selectbox("Color Palette", color_palettes)

# Chart type selector
chart_type = st.sidebar.radio("📊 Select Chart Type", ["Bar Chart", "Line Chart", "Pie Chart"])

# Display section
st.subheader(f"📊 {chart_type} - Horsepower for {selected_brand}")

if not filtered_df.empty:
    # Sort by horsepower for cleaner visual
    sorted_df = filtered_df
