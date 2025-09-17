import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Streamlit page config
st.set_page_config(page_title="Car Horsepower Explorer", layout="wide")

# Load data with caching
@st.cache_data
def load_data():
    df = pd.read_csv("CARS.csv")
    return df

df = load_data()

# Title
st.title("🚗 Car Horsepower Visualizer")
st.markdown("Explore horsepower across different **car models and brands** with customizable filters and color themes.")

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

# Optional model selection
models = sorted(filtered_df["Model"].unique())
selected_models = st.sidebar.multiselect("Select Models (optional)", models, default=models)
filtered_df = filtered_df[filtered_df["Model"].isin(selected_models)]

# 🎨 Color palette selector
st.sidebar.markdown("---")
st.sidebar.subheader("🎨 Select Color Shade")
color_palettes = [
    "viridis", "plasma", "inferno", "magma", "cividis",
    "coolwarm", "Spectral", "cubehelix", "Blues", "Greens", "Oranges", "Purples"
]
selected_palette = st.sidebar.selectbox("Color Palette", color_palettes)

# Main chart
st.subheader(f"📊 Horsepower of {selected_brand} Models")

if not filtered_df.empty:
    plt.figure(figsize=(5, 6))
    color_map = sns.color_palette(selected_palette, len(filtered_df))
    sns.barplot(
        data=filtered_df,
        x="Model",
        y="Horsepower",
        palette=color_map
    )
    plt.xticks(rotation=90)
    plt.title(f"Horsepower Comparison - {selected_brand}", fontsize=14)
    plt.ylabel("Horsepower")
    plt.xlabel("Model")
    st.pyplot(plt)
else:
    st.warning("⚠️ No data found for the selected options.")

# Optional: show filtered data
with st.expander("📋 View Filtered Data"):
    st.dataframe(filtered_df.reset_index(drop=True))
