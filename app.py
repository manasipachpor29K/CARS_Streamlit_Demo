import streamlit as st
import pandas as pd
import altair as alt

# Example dataframe (replace with your actual data)
df = pd.read_csv("cars.csv")

# Sidebar filters
hp_range = st.sidebar.slider("Select Horsepower Range", 50, 500, (200, 290))
models = st.sidebar.multiselect("Select Models (optional)", df['Model'].unique())

# Color palette
palette = st.sidebar.selectbox("Color Palette", ["viridis", "plasma", "magma", "cividis"])

# Filter data
filtered_df = df[(df['Horsepower'] >= hp_range[0]) & (df['Horsepower'] <= hp_range[1])]

if models:
    filtered_df = filtered_df[filtered_df['Model'].isin(models)]

# Title
st.title("🚗 Car Horsepower Visualizer")
st.write("Use the sidebar to filter data, choose color palettes, and explore horsepower across models.")

# Line chart
st.subheader(f"📊 Line Chart - Horsepower {f'for {', '.join(models)}' if models else ''}")

if not filtered_df.empty:
    chart = (
        alt.Chart(filtered_df)
        .mark_line(point=True)
        .encode(
            x="Model:N",
            y="Horsepower:Q",
            color=alt.Color("Model:N", scale=alt.Scale(scheme=palette))  # 👈 Apply selected palette
        )
    )
    st.altair_chart(chart, use_container_width=True)
else:
    st.warning("⚠️ No data available for the selected filters.")
