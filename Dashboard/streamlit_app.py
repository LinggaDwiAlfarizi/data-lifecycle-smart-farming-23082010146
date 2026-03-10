import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Smart Farming Dashboard", layout="wide")

st.title("🌱 Smart Farming Sensor Dashboard")
st.write("Monitoring Soil Moisture Sensor from Plant Vase")

# ===============================
# LOAD DATA
# ===============================

@st.cache_data
def load_data():
    df = pd.read_csv("../outputs/cleaned_data.csv")
    df['datetime'] = pd.to_datetime(df['datetime'])
    return df

df = load_data()

moisture_cols = ['moisture0','moisture1','moisture2','moisture3','moisture4']

# ===============================
# SIDEBAR
# ===============================

st.sidebar.header("Dashboard Settings")

sensor = st.sidebar.selectbox(
    "Select Sensor",
    moisture_cols
)

threshold = st.sidebar.slider(
    "Dry Threshold",
    min_value=0,
    max_value=100,
    value=30
)

# ===============================
# KPI METRICS
# ===============================

avg_moisture = df[sensor].mean()
min_moisture = df[sensor].min()
max_moisture = df[sensor].max()
total_records = len(df)

st.subheader("📊 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Average Moisture", f"{avg_moisture:.2f}")
col2.metric("Minimum Moisture", f"{min_moisture:.2f}")
col3.metric("Maximum Moisture", f"{max_moisture:.2f}")
col4.metric("Total Records", total_records)

st.divider()

# ===============================
# GAUGE CHART
# ===============================

latest_value = df[sensor].iloc[-1]

st.subheader("💧 Current Moisture Level")

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=latest_value,
    title={'text': sensor},
    gauge={
        'axis': {'range': [0,100]},
        'bar': {'color': "green"},
        'steps': [
            {'range': [0, threshold], 'color': "red"},
            {'range': [threshold, 60], 'color': "yellow"},
            {'range': [60, 100], 'color': "lightgreen"}
        ],
    }
))

st.plotly_chart(fig, use_container_width=True)

# ===============================
# ALERT SYSTEM
# ===============================

if latest_value < threshold:
    st.error("⚠️ Soil is too dry! Watering recommended.")
elif latest_value < 60:
    st.warning("🌤 Soil moisture is moderate.")
else:
    st.success("✅ Soil moisture is optimal.")

st.divider()

# ===============================
# TIME SERIES
# ===============================

st.subheader("📈 Moisture Trend Over Time")

fig_line = px.line(
    df,
    x="datetime",
    y=moisture_cols,
    title="Sensor Moisture Trend"
)

st.plotly_chart(fig_line, use_container_width=True)

# ===============================
# CORRELATION HEATMAP
# ===============================

st.subheader("🔥 Sensor Correlation")

fig2, ax = plt.subplots(figsize=(8,6))

sns.heatmap(
    df[moisture_cols].corr(),
    annot=True,
    cmap="coolwarm",
    ax=ax
)

st.pyplot(fig2)

# ===============================
# DISTRIBUTION
# ===============================

st.subheader("📊 Moisture Distribution")

fig_hist = px.histogram(
    df,
    x=sensor,
    nbins=30,
    title=f"Distribution of {sensor}"
)

st.plotly_chart(fig_hist, use_container_width=True)

# ===============================
# BOXPLOT SENSOR COMPARISON
# ===============================

st.subheader("📦 Sensor Comparison")

fig_box = px.box(
    df,
    y=moisture_cols,
    title="Moisture Comparison Between Sensors"
)

st.plotly_chart(fig_box, use_container_width=True)