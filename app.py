import streamlit as st
import pandas as pd
import altair as alt

# Load CSV from GitHub
csv_url = "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/cars.csv"
df = pd.read_csv(Cars.csv)

# Sidebar filters
st.sidebar.header("Filter Options")
hp_range = st.sidebar.slider("Select Horsepower Range", int(df['Horsepower'].min()), int(df['Horsepower'].max()),
                             (int(df['Horsepower'].min()), int(df['Horsepower'].max())))
models = st.sidebar.multiselect("Select Models (optional)", df['Model'].unique())
palette = st.sidebar.selectbox("Color Palette", ["viridis", "plasma", "magma", "cividis"])

# Filter data
filtered_df = df[(df['Horsepower'] >= hp_range[0]) & (df['Horsepower'] <= hp_range[1])]
if models:
    filtered_df = filtered_df[filtered_df['Model'].isin(models)]

# Title
st.title("🚗 Creative Car Horsepower Bar Plot")
st.write("Explore horsepower of car models with a colorful, interactive bar chart.")

# Bar chart
if not filtered_df.empty:
    chart = alt.Chart(filtered_df).mark_bar(cornerRadiusTopLeft=5, cornerRadiusTopRight=5).encode(
        x=alt.X("Model:N", sort='-y', title="Car Model"),
        y=alt.Y("Horsepower:Q", title="Horsepower"),
        color=alt.Color("Horsepower:Q", scale=alt.Scale(scheme=palette), title="HP"),
        tooltip=["Model", "Horsepower"]
    ).properties(
        width=700,
        height=400
    ).interactive()

    st.altair_chart(chart, use_container_width=True)
else:
    st.warning("⚠️ No data available for the selected filters.")
