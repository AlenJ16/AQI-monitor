import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import datetime

# page config 
st.set_page_config(page_title="AQI Monitor", layout="wide", page_icon="🌫")

# css part 
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style>
:root {
    --bg-base:    #1e2130;
    --bg-card:    #252838;
    --bg-sidebar: #1a1d2e;
    --bg-input:   #2d3148;
    --accent:     #5b8dee;
    --accent-dim: #3d6fd4;
    --border:     #363a52;
    --border-lt:  #444868;
    --text-hi:    #eef0f8;
    --text-mid:   #a0a8c8;
    --text-lo:    #6b7196;
    --shadow:     0 2px 10px rgba(0,0,0,0.35);
}

html, body, .stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="stMainBlockContainer"],
[data-testid="block-container"],
[class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    background-color: var(--bg-base) !important;
    color: var(--text-hi) !important;
}

p, span, li, td, th, div, label { color: var(--text-hi) !important; }

h1, h2, h3 {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 700 !important;
    color: var(--text-hi) !important;
    letter-spacing: -0.01em;
}
h4, h5, h6 { color: var(--text-mid) !important; }

section[data-testid="stSidebar"] {
    background: var(--bg-sidebar) !important;
    border-right: 1px solid var(--border) !important;
}
section[data-testid="stSidebar"] * { color: var(--text-hi) !important; }
section[data-testid="stSidebar"] .stRadio label {
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 7px 13px;
    margin: 3px 0;
    transition: all 0.18s ease;
    cursor: pointer;
    display: block;
    background: transparent;
}
section[data-testid="stSidebar"] .stRadio label:hover {
    border-color: var(--accent);
    background: rgba(91,141,238,0.10);
}

.main .block-container {
    background: var(--bg-base) !important;
    padding-top: 1.5rem !important;
}

div[data-testid="stMetric"] {
    background: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    padding: 18px 20px !important;
    box-shadow: var(--shadow) !important;
    transition: all 0.2s ease !important;
}
div[data-testid="stMetric"]:hover {
    border-color: var(--accent) !important;
    transform: translateY(-2px) !important;
}
div[data-testid="stMetricLabel"] p {
    color: var(--text-lo) !important;
    font-size: 0.75rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.08em !important;
    font-weight: 600 !important;
}
div[data-testid="stMetricValue"] {
    color: var(--accent) !important;
    font-weight: 700 !important;
    font-size: 1.9rem !important;
}

.stButton > button, .stFormSubmitButton > button {
    background: var(--accent) !important;
    color: #ffffff !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.88rem !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 10px 28px !important;
    box-shadow: 0 2px 10px rgba(91,141,238,0.3) !important;
    transition: all 0.18s ease !important;
}
.stButton > button:hover, .stFormSubmitButton > button:hover {
    background: var(--accent-dim) !important;
    transform: translateY(-1px) !important;
}

input[type="number"], input[type="text"], .stTextInput input {
    background: var(--bg-input) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    color: var(--text-hi) !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}
input:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 3px rgba(91,141,238,0.15) !important;
}

div[data-baseweb="select"] > div,
div[data-baseweb="select"] {
    background-color: var(--bg-input) !important;
    border-color: var(--border) !important;
    color: var(--text-hi) !important;
}
div[data-baseweb="select"] span { color: var(--text-hi) !important; }
div[data-baseweb="select"] svg { fill: var(--text-mid) !important; }
div[data-baseweb="popover"],
div[data-baseweb="menu"],
ul[data-testid="stSelectboxVirtualDropdown"] {
    background-color: var(--bg-card) !important;
    border: 1px solid var(--border-lt) !important;
}
li[role="option"] {
    background-color: var(--bg-card) !important;
    color: var(--text-hi) !important;
}
li[role="option"]:hover { background-color: var(--bg-input) !important; }

/* File Uploader */
[data-testid="stFileUploader"] {
    width: 100% !important;
}
[data-testid="stFileUploadDropzone"] {
    background: var(--bg-input) !important;
    border: 2px dashed var(--border-lt) !important;
    border-radius: 10px !important;
    width: 100% !important;
    padding: 1.2rem 1.5rem !important;
    box-sizing: border-box !important;
    display: flex !important;
    flex-direction: row !important;
    align-items: center !important;
    justify-content: space-between !important;
    gap: 1rem !important;
}
[data-testid="stFileUploadDropzone"] > div {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
    width: auto !important;
    flex: 1 !important;
}
[data-testid="stFileUploaderDropzoneInstructions"] {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
}
[data-testid="stFileUploaderDropzoneInstructions"] * {
    color: var(--text-mid) !important;
}
[data-testid="stFileUploadDropzone"] button {
    background: var(--accent) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 6px !important;
    white-space: nowrap !important;
    flex-shrink: 0 !important;
}

.stTable, .stDataFrame {
    background: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    overflow: hidden;
}

div[data-testid="stAlert"] {
    border-radius: 10px !important;
    border-left-width: 4px !important;
    background: var(--bg-card) !important;
}

.stDownloadButton > button {
    background: transparent !important;
    border: 1px solid var(--border-lt) !important;
    color: var(--text-mid) !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    border-radius: 8px !important;
    transition: all 0.18s ease !important;
    width: 100% !important;
    padding: 10px 28px !important;
    font-size: 0.88rem !important;
    font-weight: 600 !important;
}
.stDownloadButton > button:hover {
    border-color: var(--accent) !important;
    color: var(--accent) !important;
}

::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: var(--bg-base); }
::-webkit-scrollbar-thumb { background: var(--border-lt); border-radius: 3px; }

hr { border-color: var(--border) !important; }

.sidebar-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    color: var(--text-hi);
    letter-spacing: -0.01em;
    padding: 10px 0 16px 0;
    border-bottom: 1px solid var(--border);
    margin-bottom: 12px;
}
</style>

<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
""", unsafe_allow_html=True)


# log system 
if "logs" not in st.session_state:
    st.session_state.logs = []

def add_log(message, level="info"):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    if level == "success":
        msg = f"✅ [{timestamp}] {message}"
    elif level == "error":
        msg = f"❌ [{timestamp}] {message}"
    else:
        msg = f"ℹ️  [{timestamp}] {message}"
    st.session_state.logs.append(msg)


# model loading
@st.cache_resource
def load_model():
    with open("aqi_pipeline.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

if "model_initial_load_done" not in st.session_state:
    add_log("Model loaded successfully", "success")
    st.session_state.model_initial_load_done = True

features = ['PM2.5', 'PM10', 'O3', 'NO2', 'CO', 'SO2']


# shared Plotly theme
PLOTLY_LAYOUT = dict(
    paper_bgcolor="rgba(30,33,48,0)",
    plot_bgcolor="rgba(37,40,56,0.7)",
    font=dict(family="Plus Jakarta Sans", color="#eef0f8"),
    title_font=dict(family="Plus Jakarta Sans", color="#eef0f8"),
    xaxis=dict(gridcolor="rgba(68,72,104,0.6)", zerolinecolor="rgba(68,72,104,0.8)", color="#a0a8c8"),
    yaxis=dict(gridcolor="rgba(68,72,104,0.6)", zerolinecolor="rgba(68,72,104,0.8)", color="#a0a8c8"),
)


# Sidebar
st.sidebar.markdown('<div class="sidebar-title">🌫 AQI MONITOR</div>', unsafe_allow_html=True)
page = st.sidebar.radio(
    "Navigate",
    ["Home", "Upload & Explore Data", "AQI Prediction", "Model Logs"],
    label_visibility="collapsed"
)
st.sidebar.markdown("---")
st.sidebar.markdown(
    '<p style="font-size:0.72rem; color:#a0a8c8; text-align:center; margin-top:12px;">'
    'Ensemble ML · Voting Regressor<br>PM2.5 · PM10 · O3 · NO2 · CO · SO2</p>',
    unsafe_allow_html=True
)

# home
if page == "Home":
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #252838 0%, #2d3148 100%);
        padding: 36px 32px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 28px;
        border: 1px solid #363a52;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    ">
        <h1 style="font-family:'Plus Jakarta Sans',sans-serif; font-weight:700; color:#eef0f8; font-size:2.2rem;
                   letter-spacing:-0.01em; margin-bottom:8px;">
            🌫 AQI MONITOR
        </h1>
        <p style="color:#a0a8c8; font-size:1rem; letter-spacing:0.01em; margin:0;">
            Air Quality Prediction &amp; Analysis Dashboard
        </p>
    </div>
    """, unsafe_allow_html=True)

    # metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("R² Score", "0.934", "Excellent fit")
    col2.metric("RMSE", "26.78", delta=None)
    col3.metric("MAE", "15.97", delta=None)

    st.markdown("---")

    # Info columns
    left, right = st.columns(2, gap="large")

    with left:
        st.markdown("""<h3 style="display:flex;align-items:center;gap:8px;">
            <span class="material-icons" style="color:#5b8dee;font-size:1.4rem;">thermostat</span>
            Understanding AQI</h3>""", unsafe_allow_html=True)
        st.markdown("""
The **Air Quality Index (AQI)** measures how polluted the air is and its health impact.
Higher values = worse air quality.
        """)

        aqi_data = {
            "Range": ["0–50", "51–100", "101–200", "201–300", "301–500"],
            "Category": ["Good", "Moderate", "Poor", "Very Poor", "Severe"],
            "Health Impact": [
                "Minimal impact",
                "Minor breathing discomfort",
                "Sensitive groups affected",
                "Respiratory illness risk",
                "Serious health effects",
            ],
        }
        st.table(pd.DataFrame(aqi_data))

    with right:
        st.markdown("""<h3 style="display:flex;align-items:center;gap:8px;">
            <span class="material-icons" style="color:#5b8dee;font-size:1.4rem;">science</span>
            Key Pollutants</h3>""", unsafe_allow_html=True)
        pollutants = [
            ("PM2.5", "Fine particles penetrating deep into lungs"),
            ("PM10",  "Causes respiratory irritation"),
            ("O₃",   "Throat & airway irritation"),
            ("NO₂",  "Linked to lung diseases"),
            ("CO",   "Reduces oxygen uptake"),
            ("SO₂",  "Causes breathing difficulties"),
        ]
        for name, desc in pollutants:
            st.markdown(f"""
            <div style="background:rgba(30,33,48,0.95); border:1px solid rgba(54,58,82,1);
                        border-radius:10px; padding:10px 14px; margin-bottom:8px;">
                <span style="font-family:'Plus Jakarta Sans',sans-serif; color:#5b8dee;
                             font-size:0.82rem; font-weight:600;">{name}</span>
                <span style="color:#a0a8c8; font-size:0.85rem; margin-left:10px;">{desc}</span>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    col_env, col_safe = st.columns(2, gap="large")

    with col_env:
        st.markdown("""<h3 style="display:flex;align-items:center;gap:8px;">
            <span class="material-icons" style="color:#5b8dee;font-size:1.4rem;">park</span>
            Environmental Impact</h3>""", unsafe_allow_html=True)
        for item in ["Damages crops and vegetation", "Contributes to climate change",
                     "Causes smog & reduced visibility", "Harms ecosystems"]:
            st.markdown(f"- {item}")

    with col_safe:
        st.markdown("""<h3 style="display:flex;align-items:center;gap:8px;">
            <span class="material-icons" style="color:#5b8dee;font-size:1.4rem;">health_and_safety</span>
            How to Stay Safe</h3>""", unsafe_allow_html=True)
        for item in ["Avoid outdoor exposure during high AQI", "Use masks (N95/N99)",
                     "Use air purifiers indoors", "Reduce vehicle usage",
                     "Support green initiatives"]:
            st.markdown(f"- {item}")


# UPLOAD & EXPLORE
elif page == "Upload & Explore Data":

    st.markdown("""<h1 style="display:flex;align-items:center;gap:10px;">
        <span class="material-icons" style="color:#5b8dee;font-size:2rem;">upload_file</span>
        Upload &amp; Explore Data</h1>""", unsafe_allow_html=True)

    file = st.file_uploader("Upload CSV", type=["csv"])

    if file:
        df = pd.read_csv(file)
        
        # global cleaning to remove empty blocks
        df = df.replace(r'^\s*$', np.nan, regex=True)
        df = df.dropna()
        
        st.dataframe(df.head())

        col = st.sidebar.selectbox("Filter Column", df.columns)

    if df[col].dtype != "object":
        # 1. Check if the column is empty or all NaNs
        if df[col].isnull().all() or len(df[col]) == 0:
            st.sidebar.warning(f"Column '{col}' has no valid data to filter.") 
            filtered_df = df
        else:
            # 2. Safely calculate min and max
            min_val = float(df[col].min())
            max_val = float(df[col].max())
            
            if min_val == max_val:
                st.sidebar.info(f"Only one value ({min_val}) found in '{col}'.")
                filtered_df = df
            else:
                val = st.sidebar.slider("Range", min_val, max_val, (min_val, max_val))
                filtered_df = df[(df[col] >= val[0]) & (df[col] <= val[1])]
    else:
        val = st.sidebar.selectbox("Value", df[col].unique())
        filtered_df = df[df[col] == val] 

        st.subheader("Filtered Data")
        st.dataframe(filtered_df)

        num_cols = filtered_df.select_dtypes(include=np.number).columns

        # histogram graph
        if len(num_cols) > 0:
            c = st.selectbox("Histogram Column", num_cols)
            clean = filtered_df[c].dropna()

            fig, ax = plt.subplots()
            ax.hist(clean)
            st.pyplot(fig)

        # Scatter plot graph
        if len(num_cols) >= 2:
            x = st.selectbox("X", num_cols)
            y = st.selectbox("Y", [i for i in num_cols if i != x])

            plot_df = filtered_df[[x,y]].dropna()

            fig = px.scatter(plot_df, x=x, y=y)
            st.plotly_chart(fig)

        # Correlation map with tables and insight
        st.subheader(" Correlation Heatmap")

        if len(num_cols) > 1:
            corr_df = filtered_df[num_cols].replace([np.inf, -np.inf], np.nan)

            if corr_df.shape[0] > 1:
                corr_matrix = corr_df.corr()

                # heatmap
                fig_corr = px.imshow(
                    corr_matrix,
                    text_auto=True,
                    aspect="auto",
                    color_continuous_scale="RdBu_r",
                    title="Feature Correlation Matrix"
                )
                st.plotly_chart(fig_corr)

                # table showing stronger correlation
                st.subheader(" Strong Correlations (|corr| > 0.7)")

                strong_corr = (
                    corr_matrix.abs()
                    .unstack()
                    .reset_index()
                )

                strong_corr.columns = ["Feature 1", "Feature 2", "Correlation"]

                strong_corr = strong_corr[
                    strong_corr["Feature 1"] != strong_corr["Feature 2"]
                ]

                strong_corr = strong_corr[
                    strong_corr["Feature 1"] < strong_corr["Feature 2"]
                ]

                strong_corr = strong_corr[
                    strong_corr["Correlation"] > 0.7
                ].sort_values(by="Correlation", ascending=False)

                if not strong_corr.empty:
                    st.dataframe(strong_corr.head(10), hide_index=True)
                else:
                    st.info("No strong correlations found.")

            else:
                st.warning("Not enough data to compute correlation.")
        else:
            st.warning("Need at least 2 numeric columns for correlation.")


# AQI PREDICTION
elif page == "AQI Prediction":

    st.markdown("""<h1 style="display:flex;align-items:center;gap:10px;">
        <span class="material-icons" style="color:#5b8dee;font-size:2rem;">track_changes</span>
        Predict AQI</h1>""", unsafe_allow_html=True)

    st.markdown("""
    <p style="color:#a0a8c8; margin-bottom:20px;">
    Enter pollutant concentrations below. The ensemble model will predict the AQI value instantly.
    </p>
    """, unsafe_allow_html=True)

    with st.form("prediction_form"):
        r1c1, r1c2 = st.columns(2)
        pm25 = r1c1.number_input("PM2.5  (μg/m³)", min_value=0.0)
        pm10 = r1c2.number_input("PM10  (μg/m³)", min_value=0.0)

        r2c1, r2c2 = st.columns(2)
        o3  = r2c1.number_input("O3  (μg/m³)",  min_value=0.0)
        no2 = r2c2.number_input("NO2 (μg/m³)", min_value=0.0)

        r3c1, r3c2 = st.columns(2)
        co  = r3c1.number_input("CO  (mg/m³)",  min_value=0.0)
        so2 = r3c2.number_input("SO2 (μg/m³)", min_value=0.0)

        submitted = st.form_submit_button("⚡ Predict AQI")

    if submitted:
        add_log("Prediction started")
        input_data = pd.DataFrame([[pm25, pm10, o3, no2, co, so2]], columns=features)
        prediction = model.predict(input_data)[0]
        add_log(f"Prediction generated: AQI = {prediction:.2f}", "success")

        # AQI category colours
        cat_map = [
            (50,  "Good",      "#00FF9D"),
            (100, "Moderate",  "#FFE600"),
            (200, "Poor",      "#FF8C00"),
            (300, "Very Poor", "#FF3B30"),
            (500, "Severe",    "#3b7dd8"),
        ]
        category, cat_color = "Severe", "#3b7dd8"
        for threshold, cat, col in cat_map:
            if prediction <= threshold:
                category, cat_color = cat, col
                break

        res_l, res_r = st.columns([1, 1], gap="large")
        with res_l:
            st.markdown(f"""
            <div style="background:rgba(37,40,56,0.95); border:1px solid {cat_color}55;
                        border-radius:16px; padding:28px; text-align:center;
                        box-shadow: 0 0 30px {cat_color}33; margin-top:16px;">
                <p style="color:#a0a8c8; font-size:0.8rem; letter-spacing:0.12em;
                           text-transform:uppercase; margin-bottom:6px;">Predicted AQI</p>
                <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:3.5rem;
                           color:{cat_color}; margin:0; text-shadow: 0 0 20px {cat_color}88;">
                    {prediction:.1f}
                </p>
                <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:1rem;
                           color:{cat_color}; letter-spacing:0.1em; margin-top:6px;">
                    {category}
                </p>
            </div>
            """, unsafe_allow_html=True)

        with res_r:
            fig_gauge = go.Figure(go.Indicator(
                mode="gauge+number",
                value=prediction,
                number={'font': {'family': 'Plus Jakarta Sans', 'color': '#3b7dd8'}},
                gauge={
                    'axis': {'range': [0, 500], 'tickcolor': '#a0a8c8',
                             'tickfont': {'color': '#a0a8c8'}},
                    'bar': {'color': cat_color, 'thickness': 0.25},
                    'bgcolor': 'rgba(37,40,56,0.95)',
                    'bordercolor': 'rgba(54,58,82,1)',
                    'steps': [
                        {'range': [0,   50],  'color': '#00c96e'},
                        {'range': [50,  100], 'color': '#f5c518'},
                        {'range': [100, 200], 'color': '#ff8c00'},
                        {'range': [200, 300], 'color': '#e03131'},
                        {'range': [300, 500], 'color': '#7048e8'},
                    ],
                    'threshold': {
                        'line': {'color': cat_color, 'width': 3},
                        'thickness': 0.75,
                        'value': prediction,
                    }
                }
            ))
            fig_gauge.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                font=dict(family="Plus Jakarta Sans", color="#1a202c"),
                height=260, margin=dict(t=20, b=10, l=20, r=20)
            )
            st.plotly_chart(fig_gauge, use_container_width=True)


# logs page
elif page == "Model Logs":

    st.markdown("""<h1 style="display:flex;align-items:center;gap:10px;">
        <span class="material-icons" style="color:#5b8dee;font-size:2rem;">assignment</span>
        Model Logs</h1>""", unsafe_allow_html=True)

    # log info banner
    st.markdown("""
    <div style="background:linear-gradient(135deg,rgba(59,125,216,0.06),rgba(59,125,216,0.04));
                border:1px solid rgba(54,58,82,1); border-radius:14px;
                padding:16px 20px; margin-bottom:20px;">
        <span style="font-family:'Plus Jakarta Sans',sans-serif; color:#5b8dee; font-size:0.95rem; font-weight:600;">
            Final Model: Voting Regressor (RF + XGB + LGBM)
        </span>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    col1.metric("R²",   "0.934")
    col2.metric("RMSE", "26.78")
    col3.metric("MAE",  "15.97")

    st.markdown("---")
    left_l, right_l = st.columns(2, gap="large")

    with left_l:
        st.markdown("#### Features Used")
        st.markdown(" · ".join(features))
        st.markdown("#### Pipeline")
        steps = ["Data Cleaning", "Training", "Ensemble", "Prediction"]
        st.markdown(" → ".join(
            [f'<span style="color:#5b8dee;font-family:Plus Jakarta Sans,sans-serif;'
             f'font-size:0.78rem;font-weight:600;">{s}</span>' for s in steps]
        ), unsafe_allow_html=True)
        st.markdown("#### Training Info")
        st.markdown("80-20 Train/Test Split · 5-Fold Cross-Validation")

    with right_l:
        comp = pd.DataFrame({
            "Model": ["RF", "XGB", "LGBM", "Stacking", "Voting"],
            "R²":    [0.9305, 0.9325, 0.9274, 0.9325, 0.9340],
        })
        fig_pie = px.pie(
            comp,
            names="Model",
            values="R²",
            title="Model Performance Comparison (R²)",
            hole=0.3,
            color_discrete_sequence=["#c0392b", "#2e7d32", "#3b7dd8", "#3b7dd8", "#2563b0"],
        )
        fig_pie.update_traces(
            textinfo='label+value+percent',
            textfont=dict(family="Plus Jakarta Sans", size=12, color="white"),
        )
        fig_pie.update_layout(
            **PLOTLY_LAYOUT,
            title=dict(
                text="Model Performance Comparison (R²)",
                font=dict(family="Plus Jakarta Sans", color="#3b7dd8", size=14),
                x=0.5,
                xanchor="center",
            ),
            legend_title="Models",
            legend=dict(
                font=dict(color="#eef0f8", size=12),
                title_font=dict(color="#a0a8c8"),
                bgcolor="rgba(37,40,56,0.8)",
                bordercolor="#444868",
                borderwidth=1,
            ),
            height=320,
            margin=dict(t=50, b=10, l=10, r=10),
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    st.markdown("---")
    st.markdown("""<h4 style="display:flex;align-items:center;gap:8px;margin-top:8px;">
        <span class="material-icons" style="color:#5b8dee;font-size:1.2rem;">receipt_long</span>
        Event Logs</h4>""", unsafe_allow_html=True)

    if st.session_state.logs:
        log_html = "".join([
            f'<div style="font-family:\'DM Mono\',monospace; font-size:0.82rem;'
            f'color:#a0a8c8; padding:5px 10px; border-left:2px solid rgba(91,141,238,0.25);'
            f'margin-bottom:4px;">{log}</div>'
            for log in reversed(st.session_state.logs)
        ])
        st.markdown(
            f'<div style="background:rgba(30,33,48,0.95); border:1px solid rgba(54,58,82,1);'
            f'border-radius:10px; padding:12px; max-height:280px; overflow-y:auto;">'
            f'{log_html}</div>',
            unsafe_allow_html=True
        )

        _, c1, c2, _ = st.columns([1, 2, 2, 1])
        st.markdown("<div style='margin-top: 16px;'></div>", unsafe_allow_html=True)
        _, c1, c2, _ = st.columns([1, 2, 2, 1])
        with c1:
            st.download_button(
                "Download Logs",
                data="\n".join(st.session_state.logs),
                file_name="aqi_logs.txt",
                mime="text/plain",
                use_container_width=True,
            )
        with c2:
            if st.button("Clear Logs", use_container_width=True):
                st.session_state.logs = []
                st.rerun()
    else:
        st.info("No logs yet. Run a prediction to see activity here.")