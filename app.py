import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="Car Horsepower Explorer", layout="wide")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("../Datasets/CARS.csv")
    return df

df = load_data()

# Title and description
st.title("🚗 Car Horsepower Visualizer")
st.markdown("Explore horsepower across different **car models and brands** with interactive filters and color-coded charts.")

# Sidebar filters
st.sidebar.header("🔍 Filters")

# Brand selection
brands = sorted(df["Make"].unique())
selected_brand = st.sidebar.selectbox("Select a Brand", brands)

# Filter by brand
filtered_df = df[df["Make"] == selected_brand]

# Optional horsepower range slider
min_hp = int(filtered_df["Horsepower"].min())
max_hp = int(filtered_df["Horsepower"].max())
hp_range = st.sidebar.slider("Select Horsepower Range", min_value=min_hp, max_value=max_hp, value=(min_hp, max_hp))

# Filtered based on HP range
filtered_df = filtered_df[(filtered_df["Horsepower"] >= hp_range[0]) & (filtered_df["Horsepower"] <= hp_range[1])]

# Optional: model multi-select
models = sorted(filtered_df["Model"].unique())
selected_models = st.sidebar.multiselect("Filter Specific Models (optional)", models, default=models)

filtered_df = filtered_df[filtered_df["Model"].isin(selected_models)]

# Plot section
st.subheader(f"🎨 Horsepower of {selected_brand} Models")

if not filtered_df.empty:
    # Create a color-coded barplot
    plt.figure(figsize=(12, 6))
    color_map = sns.color_palette("coolwarm", len(filtered_df))
    sns.barplot(
        data=filtered_df,
        x="Model",
        y="Horsepower",
        palette=color_map
    )
    plt.xticks(rotation=90)
    plt.title(f"Horsepower Comparison: {selected_brand}", fontsize=14)
    plt.ylabel("Horsepower")
    plt.xlabel("Model")
    st.pyplot(plt)
else:
    st.warning("⚠️ No data available for the selected brand and filters.")

# Show table below
with st.expander("📋 View Filtered Data"):
    st.dataframe(filtered_df.reset_index(drop=True))


