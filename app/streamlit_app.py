"""Client satisfaction analytics dashboard — D08."""

import sys
from pathlib import Path

import joblib
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from features import FEATURE_COLUMNS, TARGET, prepare_features

st.set_page_config(page_title="business-analysis-project", page_icon="📊", layout="wide")

st.title("Business Analysis Project")
st.caption("What predicts satisfied enterprise clients? — Account Director view")

DATA_PATH = Path("data/client_satisfaction.csv")
MODEL_PATH = Path("models/model.joblib")

if not DATA_PATH.exists():
    st.warning("Dataset not found. Run `python src/train.py` first.")
    st.stop()

df = pd.read_csv(DATA_PATH)
df["satisfied_label"] = df[TARGET].map({0: "At risk", 1: "Satisfied"})

# --- Sidebar filters ---
st.sidebar.header("Filters")
nps_range = st.sidebar.slider("NPS score range", 0, 100, (int(df["nps_score"].min()), int(df["nps_score"].max())))
max_response = st.sidebar.slider("Max response time (hrs)", 0.0, float(df["response_time_hrs"].max()), float(df["response_time_hrs"].max()))
escalation_cap = st.sidebar.slider("Max escalations", 0.0, float(df["escalations"].max()), float(df["escalations"].max()))

filtered = df[
    (df["nps_score"].between(nps_range[0], nps_range[1]))
    & (df["response_time_hrs"] <= max_response)
    & (df["escalations"] <= escalation_cap)
]

# --- KPI row ---
c1, c2, c3, c4 = st.columns(4)
sat_rate = filtered[TARGET].mean() * 100 if len(filtered) else 0
c1.metric("Clients in view", f"{len(filtered):,}", f"{len(filtered) - len(df):+,} vs full")
c2.metric("Satisfaction rate", f"{sat_rate:.1f}%")
c3.metric("Avg NPS", f"{filtered['nps_score'].mean():.1f}" if len(filtered) else "—")
c4.metric("Avg response (hrs)", f"{filtered['response_time_hrs'].mean():.1f}" if len(filtered) else "—")

tab_overview, tab_trends, tab_predict = st.tabs(["Overview", "Trends & drill-down", "ML predictions"])

with tab_overview:
    left, right = st.columns(2)
    with left:
        fig_nps = px.histogram(
            filtered, x="nps_score", color="satisfied_label",
            nbins=20, barmode="overlay", opacity=0.75,
            title="NPS distribution by satisfaction",
            color_discrete_map={"Satisfied": "#2ecc71", "At risk": "#e74c3c"},
        )
        st.plotly_chart(fig_nps, use_container_width=True)
    with right:
        fig_pie = px.pie(
            filtered, names="satisfied_label", title="Satisfaction mix",
            color="satisfied_label",
            color_discrete_map={"Satisfied": "#2ecc71", "At risk": "#e74c3c"},
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    fig_scatter = px.scatter(
        filtered, x="response_time_hrs", y="nps_score", color="satisfied_label",
        size="escalations", hover_data=["client_id", "escalations"],
        title="Response time vs NPS (size = escalations)",
        color_discrete_map={"Satisfied": "#2ecc71", "At risk": "#e74c3c"},
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

with tab_trends:
    trend = filtered.copy()
    trend["client_order"] = range(1, len(trend) + 1)
    fig_trend = px.line(
        trend, x="client_order", y="nps_score", color="satisfied_label",
        markers=True, title="NPS trajectory across client cohort",
    )
    st.plotly_chart(fig_trend, use_container_width=True)

    fig_esc = px.box(filtered, x="satisfied_label", y="escalations", color="satisfied_label",
                     title="Escalation volume by satisfaction outcome",
                     color_discrete_map={"Satisfied": "#2ecc71", "At risk": "#e74c3c"})
    st.plotly_chart(fig_esc, use_container_width=True)

with tab_predict:
    if not MODEL_PATH.exists():
        st.info("Train a model first: `python src/train.py`")
    else:
        model = joblib.load(MODEL_PATH)
        X, y_true = prepare_features(filtered)
        preds = model.predict(X)
        proba = model.predict_proba(X)[:, 1] if hasattr(model, "predict_proba") else preds.astype(float)

        result = filtered.copy()
        result["predicted"] = preds
        result["p_satisfied"] = proba

        sel = st.selectbox("Inspect client", result["client_id"].astype(str).tolist())
        row = result[result["client_id"].astype(str) == sel].iloc[0]
        g1, g2, g3 = st.columns(3)
        g1.metric("Actual", "Satisfied" if row[TARGET] == 1 else "At risk")
        g2.metric("Predicted", "Satisfied" if row["predicted"] == 1 else "At risk")
        g3.metric("P(satisfied)", f"{row['p_satisfied']:.0%}")

        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number", value=row["p_satisfied"] * 100,
            title={"text": f"Client {sel} — satisfaction likelihood"},
            gauge={"axis": {"range": [0, 100]}, "bar": {"color": "#3498db"},
                   "steps": [{"range": [0, 50], "color": "#fadbd8"}, {"range": [50, 100], "color": "#d5f5e3"}]},
        ))
        st.plotly_chart(fig_gauge, use_container_width=True)

        fig_prob = px.histogram(result, x="p_satisfied", nbins=25, title="Model confidence distribution")
        st.plotly_chart(fig_prob, use_container_width=True)

        st.dataframe(
            result[["client_id", "nps_score", "response_time_hrs", "escalations", TARGET, "predicted", "p_satisfied"]]
            .sort_values("p_satisfied", ascending=False)
            .head(25),
            use_container_width=True,
        )
