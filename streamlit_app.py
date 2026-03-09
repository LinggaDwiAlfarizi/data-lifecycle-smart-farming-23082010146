import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

st.set_page_config(page_title="Plant Moisture Dashboard", layout="wide")

st.title("🌱 Plant Vase Sensor Dashboard")

# ==========================
# Upload Dataset
# ==========================

uploaded_file = st.file_uploader("Upload cleaned_data.csv", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)
    df['datetime'] = pd.to_datetime(df['datetime'])

    moisture_cols = ['moisture0','moisture1','moisture2','moisture3','moisture4']

    # ==========================
    # SIDEBAR
    # ==========================

    st.sidebar.title("Dashboard Settings")

    selected_sensor = st.sidebar.selectbox(
        "Select Sensor",
        moisture_cols
    )

    threshold = st.sidebar.slider(
        "Alert Threshold",
        min_value=0,
        max_value=100,
        value=30
    )

    # ==========================
    # DATA QUALITY METRICS
    # ==========================

    accuracy = (1 - (df.isnull().sum().sum() / df.size)) * 100
    completeness = (df.count().sum() / df.size) * 100
    total_data = df.shape[0]

    st.subheader("📊 Data Quality Metrics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Accuracy", f"{accuracy:.2f}%")
    col2.metric("Completeness", f"{completeness:.2f}%")
    col3.metric("Total Records", total_data)

    st.divider()

    # ==========================
    # GAUGE METER
    # ==========================

    latest_value = df[selected_sensor].iloc[-1]

    st.subheader("💧 Current Moisture Level")

    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=latest_value,
        title={'text': selected_sensor},
        gauge={
            'axis': {'range': [0,100]},
            'bar': {'color': "green"},
            'steps': [
                {'range': [0, threshold], 'color': "red"},
                {'range': [threshold, 100], 'color': "lightgreen"}
            ],
        }
    ))

    st.plotly_chart(fig_gauge, use_container_width=True)

    # ==========================
    # ALERT SYSTEM
    # ==========================

    if latest_value < threshold:
        st.error(f"⚠️ ALERT: Moisture {selected_sensor} is below threshold!")
    else:
        st.success("✅ Moisture level is safe")

    st.divider()

    # ==========================
    # TIME SERIES
    # ==========================

    st.subheader("📈 Moisture Sensor Trend")

    fig, ax = plt.subplots(figsize=(12,5))

    for col in moisture_cols:
        ax.plot(df['datetime'], df[col], label=col)

    ax.legend()
    ax.set_xlabel("Time")
    ax.set_ylabel("Moisture")

    st.pyplot(fig)

    # ==========================
    # HEATMAP CORRELATION
    # ==========================

    st.subheader("🔥 Sensor Correlation Heatmap")

    fig2, ax2 = plt.subplots(figsize=(8,6))

    sns.heatmap(df[moisture_cols].corr(),
                annot=True,
                cmap='coolwarm',
                ax=ax2)

    st.pyplot(fig2)

    # ==========================
    # DISTRIBUTION
    # ==========================

    st.subheader("📊 Sensor Distribution")

    fig3, ax3 = plt.subplots()

    sns.histplot(df[selected_sensor], kde=True, ax=ax3)

    st.pyplot(fig3)

    # ==========================
    # BOX COMPARISON
    # ==========================

    st.subheader("📦 Sensor Comparison")

    fig4, ax4 = plt.subplots()

    sns.boxplot(data=df[moisture_cols], ax=ax4)

    st.pyplot(fig4)

else:
    st.info("Please upload cleaned_data.csv")
