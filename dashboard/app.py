import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# =====================================================
# Page config
# =====================================================
st.set_page_config(
    page_title="Ethiopia Financial Inclusion Dashboard",
    layout="wide"
)

# =====================================================
# Data loading
# =====================================================
@st.cache_data
def load_data(path):
    try:
        return pd.read_excel(path, sheet_name="ethiopia_fi_unified_data")
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        return pd.DataFrame()

DATA_PATH = "../data/processed/ethiopia_fi_unified_data_enriched.xlsx"
df = load_data(DATA_PATH)

if df.empty:
    st.stop()

# =====================================================
# Common preprocessing
# =====================================================
def prepare_access(df):
    data = df[
        (df["indicator_code"] == "ACC_OWNERSHIP") &
        (df["value_numeric"].notna())
    ][["observation_date", "value_numeric"]].copy()

    data["year"] = pd.to_datetime(data["observation_date"]).dt.year
    return data.sort_values("year")

access = prepare_access(df)

# =====================================================
# Forecast preparation (GLOBAL, reusable)
# =====================================================
def fit_trend(data):
    if len(data) < 2:
        return None
    X = data["year"].values.reshape(-1, 1)
    y = data["value_numeric"].values
    model = LinearRegression()
    model.fit(X, y)
    return model

forecast_df = pd.DataFrame()

access_model = fit_trend(access)
if access_model is not None:
    forecast_years = np.array([2025, 2026, 2027]).reshape(-1, 1)
    baseline = access_model.predict(forecast_years)

    scenarios = {
        "Pessimistic": -1.5,
        "Base": 0.0,
        "Optimistic": 2.0
    }

    rows = []
    for s, adj in scenarios.items():
        for i, y in enumerate([2025, 2026, 2027]):
            rows.append({
                "Year": y,
                "Scenario": s,
                "Account Ownership (%)": round(baseline[i] + adj, 2)
            })

    forecast_df = pd.DataFrame(rows)

# =====================================================
# Sidebar
# =====================================================
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Overview", "Trends", "Forecasts", "Inclusion Projections"]
)

# =====================================================
# Overview Page
# =====================================================
if page == "Overview":
    st.title("Overview of Financial Inclusion in Ethiopia")

    col1, col2, col3 = st.columns(3)

    with col1:
        if not access.empty:
            st.metric(
                "Account Ownership (%)",
                round(access.iloc[-1]["value_numeric"], 1)
            )
        else:
            st.metric("Account Ownership (%)", "Data unavailable")

    with col2:
        st.metric("Digital Payment Usage (%)", "Data unavailable")
        st.caption("No survey-based usage percentage available; proxies used elsewhere")

    with col3:
        p2p = df[df["indicator_code"] == "USG_P2P_COUNT"]["value_numeric"].sum()
        atm = df[df["indicator_code"] == "USG_ATM_COUNT"]["value_numeric"].sum()
        ratio = round(p2p / atm, 2) if atm > 0 else "N/A"
        st.metric("P2P / ATM Crossover Ratio", ratio)

    st.markdown("""
    **Key insights**
    - Account ownership has grown steadily since 2014  
    - Digital finance accelerated after Telebirr (2021)  
    - P2P usage increasingly substitutes ATM withdrawals  
    """)

# =====================================================
# Trends Page
# =====================================================
elif page == "Trends":
    st.title("Trends Over Time")

    start, end = st.slider(
        "Select year range",
        int(access["year"].min()),
        int(access["year"].max()),
        (int(access["year"].min()), int(access["year"].max()))
    )

    subset = access[(access["year"] >= start) & (access["year"] <= end)]

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(subset["year"], subset["value_numeric"], marker="o")
    ax.set_title("Account Ownership Trend")
    ax.set_xlabel("Year")
    ax.set_ylabel("% of Adults")
    ax.grid(True)
    st.pyplot(fig)

    st.caption(
    "⚠ Channel-level comparisons (e.g., ATM vs P2P vs mobile payments) "
    "are limited due to inconsistent historical coverage across indicators."
    )

# =====================================================
# Forecasts Page
# =====================================================
elif page == "Forecasts":
    st.title("Forecasts (2025–2027)")

    if forecast_df.empty:
        st.warning("Forecast not available due to insufficient data.")
    else:
        st.dataframe(forecast_df, use_container_width=True)

        fig, ax = plt.subplots(figsize=(9, 4))
        for s in forecast_df["Scenario"].unique():
            d = forecast_df[forecast_df["Scenario"] == s]
            ax.plot(d["Year"], d["Account Ownership (%)"], marker="o", label=s)

        ax.set_title("Account Ownership Forecast Scenarios")
        ax.set_xlabel("Year")
        ax.set_ylabel("% of Adults")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)

# =====================================================
# Inclusion Projections Page
# =====================================================
elif page == "Inclusion Projections":
    st.title("Progress Toward 60% Financial Inclusion Target")

    if forecast_df.empty:
        st.warning("Forecast data not available.")
        st.stop()

    target = 60

    fig, ax = plt.subplots(figsize=(9, 4))
    for s in forecast_df["Scenario"].unique():
        d = forecast_df[forecast_df["Scenario"] == s]
        ax.plot(d["Year"], d["Account Ownership (%)"], marker="o", label=s)

    ax.axhline(target, linestyle="--", color="red", label="60% Target")
    ax.set_xlabel("Year")
    ax.set_ylabel("Account Ownership (%)")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    st.markdown("""
    **Key uncertainties**
    - Sparse household survey data  
    - Policy and regulatory shifts  
    - Speed of digital adoption  

    **Largest potential impact**
    - Mobile money expansion  
    - Government digital payment programs  

    **Limitations**
    - Linear trend assumption  
    - Usage measured via proxy indicators  
    """)

    st.download_button(
        "Download forecast table",
        forecast_df.to_csv(index=False),
        file_name="ethiopia_inclusion_forecast.csv"
    )
