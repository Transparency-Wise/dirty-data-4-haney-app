"""
Haney Soil Health Analysis Dashboard - Home Page
Welcome and navigation portal for the analysis platform

Developed in partnership with Regen Ag Lab
"""

import streamlit as st
from pathlib import Path
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Haney Soil Health Dashboard - Home",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS - Regen Ag Lab Brand Styling
st.markdown("""
<style>
    /* Import Raleway font */
    @import url('https://fonts.googleapis.com/css2?family=Raleway:wght@400;600;700&display=swap');

    /* CSS Variables matching Regen Ag Lab brand */
    :root {
        --color-primary: #e40032;
        --color-dark: #53575a;
        --color-light-bg: #f5f5f5;
        --color-white: #ffffff;
        --font-family: 'Raleway', sans-serif;
        --border-radius: 5px;
    }

    /* Override Streamlit defaults */
    .stApp {
        background-color: #f5f5f5 !important;
    }

    .main .block-container {
        background-color: #f5f5f5 !important;
    }

    html, body, [class*="css"], .stMarkdown {
        font-family: 'Raleway', sans-serif !important;
        font-size: 17px;
        line-height: 1.7;
        color: #53575a;
    }

    /* Headings */
    h1, h2, h3, h4 {
        font-family: 'Raleway', sans-serif !important;
        font-weight: 600 !important;
        color: #53575a !important;
    }

    /* Hero Section */
    .hero-section {
        background: #ffffff;
        padding: 4rem 3rem;
        border-radius: 0;
        margin-bottom: 3rem;
        text-align: center;
        border: none;
    }

    .hero-title {
        font-size: 52px;
        color: #53575a;
        font-weight: 600;
        margin-bottom: 1.5rem;
        font-family: 'Raleway', sans-serif;
        line-height: 1.3;
    }

    .hero-subtitle {
        font-size: 24px;
        color: #464646;
        margin-bottom: 1rem;
        font-family: 'Raleway', sans-serif;
        font-weight: 400;
        line-height: 1.6;
    }

    .hero-tagline {
        font-size: 18px;
        color: #e40032;
        font-weight: 600;
        margin-top: 1.5rem;
        font-family: 'Raleway', sans-serif;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Methodology cards */
    .methodology-card {
        background-color: #ffffff;
        padding: 35px 30px;
        border-radius: 5px;
        border-left: 5px solid #e40032;
        margin: 1.5rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }

    .methodology-card h3 {
        color: #53575a !important;
        font-size: 26px !important;
        margin-top: 0 !important;
        margin-bottom: 15px !important;
    }

    .methodology-card h4 {
        color: #e40032 !important;
        font-size: 20px !important;
        margin-top: 25px !important;
    }

    .methodology-card p {
        font-size: 17px !important;
        line-height: 1.7 !important;
        color: #53575a !important;
    }

    /* Section backgrounds */
    .section-light {
        background-color: #f5f5f5;
        padding: 60px 40px;
        margin: 40px -40px;
        border-radius: 0;
    }

    .section-white {
        background-color: #ffffff;
        padding: 60px 40px;
        margin: 40px -40px;
    }

    /* Feature cards - matching Regen Ag Lab service cards */
    .feature-card {
        background-color: #ffffff;
        padding: 40px 30px;
        border-radius: 5px;
        border: none;
        height: 100%;
        transition: all 0.3s ease;
        text-align: center;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
    }

    .feature-card:hover {
        box-shadow: 0 6px 20px rgba(228, 0, 50, 0.2);
        transform: translateY(-5px);
    }

    .feature-card h4 {
        color: #53575a !important;
        font-size: 22px !important;
        margin-bottom: 15px !important;
        font-weight: 600 !important;
    }

    .feature-card p {
        color: #53575a !important;
        font-size: 16px !important;
        line-height: 1.7 !important;
    }

    .feature-icon {
        font-size: 60px;
        margin-bottom: 20px;
        display: block;
    }

    /* Stats cards */
    .stats-highlight {
        background-color: #f5f5f5;
        padding: 35px 25px;
        border-radius: 5px;
        border: none;
        text-align: center;
        transition: all 0.3s ease;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }

    .stats-highlight:hover {
        background-color: #ffffff;
        box-shadow: 0 4px 12px rgba(228, 0, 50, 0.12);
        transform: translateY(-2px);
    }

    .stats-highlight h2 {
        color: #53575a !important;
        font-size: 48px !important;
        margin: 0 !important;
        font-weight: 700 !important;
    }

    .stats-highlight p {
        color: #464646 !important;
        font-size: 15px !important;
        margin: 12px 0 0 0 !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-weight: 600;
    }

    /* Buttons */
    .regen-button {
        background-color: #53575a;
        color: #ffffff !important;
        font-family: 'Raleway', sans-serif;
        font-size: 16px;
        font-weight: 600;
        padding: 16px 35px;
        border-radius: 5px;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s ease;
        text-decoration: none !important;
        display: inline-block;
    }

    .regen-button:hover {
        background-color: #e40032;
        color: #ffffff !important;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.15);
    }

    /* Links */
    a {
        color: #e40032;
        text-decoration: none;
        transition: color 0.2s ease;
    }

    a:hover {
        color: #3a3a3a;
        text-decoration: underline;
    }

    /* Sidebar styling - allow it to be toggled */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
    }

    /* Top Navigation Bar */
    .top-nav {
        background-color: #ffffff;
        border-bottom: 3px solid #e40032;
        padding: 0;
        margin: 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        width: 100%;
        z-index: 999;
        font-family: 'Raleway', sans-serif;
    }

    /* Add padding to main content to account for fixed navbar */
    .block-container {
        padding-top: 80px !important;
    }

    .nav-container {
        max-width: 1240px;
        margin: 0 auto;
        display: flex;
        align-items: center;
        padding: 0 20px;
    }

    .nav-logo {
        font-size: 24px;
        font-weight: 600;
        color: #e40032;
        padding: 15px 20px 15px 0;
        text-decoration: none;
    }

    .nav-menu {
        display: flex;
        list-style: none;
        margin: 0;
        padding: 0;
        flex-grow: 1;
    }

    .nav-item {
        position: relative;
    }

    .nav-link {
        display: block;
        padding: 18px 20px;
        color: #53575a !important;
        text-decoration: none !important;
        font-weight: 600;
        font-size: 16px;
        transition: all 0.2s ease;
        cursor: pointer;
    }

    .nav-link:visited {
        color: #53575a !important;
        text-decoration: none !important;
    }

    .nav-link:hover {
        background-color: #f5f5f5;
        color: #e40032 !important;
        text-decoration: none !important;
    }

    .nav-link.active {
        background-color: #e40032;
        color: #ffffff !important;
    }

    /* Dropdown menu */
    .dropdown {
        position: relative;
        display: inline-block;
    }

    .dropdown-content {
        display: none;
        position: absolute;
        background-color: #ffffff;
        min-width: 250px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        z-index: 1000;
        border: 1px solid #eaeaea;
        border-top: 3px solid #e40032;
    }

    .dropdown:hover .dropdown-content {
        display: block;
    }

    .dropdown-content a {
        color: #53575a;
        padding: 12px 20px;
        text-decoration: none;
        display: block;
        font-size: 15px;
        font-weight: 400;
        transition: all 0.2s ease;
    }

    .dropdown-content a:hover {
        background-color: #f5f5f5;
        color: #e40032;
        padding-left: 25px;
    }

    .dropdown-arrow {
        font-size: 12px;
        margin-left: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Navigation Bar with dropdown - Deployment Ready (Hybrid approach)
st.markdown("""
<style>
    /* Navigation bar container */
    [data-testid="stHorizontalBlock"]:first-of-type {
        background-color: #ffffff;
        border-bottom: 3px solid #e40032;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        padding: 10px 20px;
        margin-top: 0;
        margin-bottom: 20px;
    }

    /* Style columns in navbar to be inline and vertically centered */
    [data-testid="stHorizontalBlock"]:first-of-type [data-testid="column"] {
        padding: 0 !important;
        display: flex !important;
        align-items: center !important;
    }

    /* Logo styling */
    .nav-logo {
        font-size: 24px;
        font-weight: 700;
        color: #e40032;
        padding: 15px 0;
        font-family: 'Raleway', sans-serif;
    }

    /* Style Streamlit page_link buttons to match navbar */
    [data-testid="stHorizontalBlock"]:first-of-type .stButton > button {
        background-color: transparent !important;
        background-image: none !important;
        border: none !important;
        box-shadow: none !important;
        outline: none !important;
        color: #53575a !important;
        font-weight: 500 !important;
        font-family: 'Raleway', sans-serif !important;
        font-size: 16px !important;
        padding: 12px 18px !important;
        transition: all 0.2s ease !important;
        border-radius: 0 !important;
        height: auto !important;
        line-height: normal !important;
        margin: 0 !important;
        text-decoration: none !important;
        cursor: pointer !important;
        display: block !important;
        min-height: 0 !important;
    }

    [data-testid="stHorizontalBlock"]:first-of-type .stButton > button:hover {
        background-color: #f5f5f5 !important;
        background-image: none !important;
        color: #e40032 !important;
        box-shadow: none !important;
        text-decoration: none !important;
    }

    [data-testid="stHorizontalBlock"]:first-of-type .stButton > button:focus {
        background-color: transparent !important;
        box-shadow: none !important;
        outline: none !important;
    }

    [data-testid="stHorizontalBlock"]:first-of-type .stButton > button:active {
        background-color: #f5f5f5 !important;
        box-shadow: none !important;
    }

    [data-testid="stHorizontalBlock"]:first-of-type .stButton {
        display: inline-block !important;
        margin: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# Navigation using columns - this becomes the sticky header
nav_cols = st.columns([1.0, 0.6, 0.9, 0.8, 0.6])

with nav_cols[0]:
    st.markdown('<div class="nav-logo">Haney Soil AI</div>', unsafe_allow_html=True)

with nav_cols[1]:
    st.page_link("pages/01_Home.py", label="Home", use_container_width=False)

with nav_cols[2]:
    st.page_link("app.py", label="Analysis Dashboard", use_container_width=False)

with nav_cols[3]:
    st.page_link("pages/02_Economic_Analysis.py", label="Economic Analysis", use_container_width=False)

with nav_cols[4]:
    st.page_link("pages/03_Feedback.py", label="Feedback", use_container_width=False)

# Sidebar navigation
st.sidebar.markdown("## Navigation")
st.sidebar.page_link("pages/01_Home.py", label="🏠 Home")
st.sidebar.page_link("pages/02_Economic_Analysis.py", label="💰 Economic Analysis")
st.sidebar.page_link("pages/03_Feedback.py", label="💬 Feedback")
st.sidebar.markdown("---")
st.sidebar.markdown("## Analysis Dashboard")
st.sidebar.page_link("app.py", label="📊 View Analysis Dashboard")

# Load logo and paths
BASE_DIR = Path(__file__).resolve().parent.parent
DASHBOARD_DIR = Path(__file__).resolve().parent.parent
LOGO_PATH = DASHBOARD_DIR / 'assets' / 'regen_ag_lab_logo.png'
DATA_FILE = BASE_DIR / 'data' / 'processed' / 'combined_soil_data_FULL.csv'

# Hero Section - Matching Regen Ag Lab homepage
st.markdown("""
<div class="hero-section">
    <div class="hero-tagline">GAIN GROUND</div>
    <div class="hero-title">Laboratory Services Focusing on<br>Soil Health & Regenerative Agriculture</div>
    <div class="hero-subtitle">
        Advanced soil health analytics using the revolutionary Haney Test methodology<br>
        to restore soil, water, and air resources through data-driven insights
    </div>
    <p style="color: #53575a; font-size: 18px; font-family: 'Raleway', sans-serif; margin-top: 2rem; max-width: 900px; margin-left: auto; margin-right: auto;">
        Developed in collaboration with <strong>Dr. Rick Haney</strong>, Chief Scientific Officer at Regen Ag Lab<br>
    </p>
</div>  
""", unsafe_allow_html=True)

try:
    import pandas as pd
    data = pd.read_csv(DATA_FILE)
    n_samples = len(data)
    n_variables = len(data.columns)
    n_batches = data['_source_batch'].nunique() if '_source_batch' in data.columns else 'Multiple'
    data_loaded = True
except Exception as e:
    n_samples = 3625
    n_variables = 139
    n_batches = 4
    data_loaded = False

# Key Stats
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stats-highlight">
        <h2 style="color: #2c5f2d; margin: 0;">{:,}</h2>
        <p style="margin: 0.5rem 0 0 0; color: #666;">Soil Samples</p>
    </div>
    """.format(n_samples), unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stats-highlight">
        <h2 style="color: #2c5f2d; margin: 0;">{}</h2>
        <p style="margin: 0.5rem 0 0 0; color: #666;">Variables Tracked</p>
    </div>
    """.format(n_variables), unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stats-highlight">
        <h2 style="color: #2c5f2d; margin: 0;">{}</h2>
        <p style="margin: 0.5rem 0 0 0; color: #666;">Data Batches</p>
    </div>
    """.format(n_batches), unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stats-highlight">
        <h2 style="color: #2c5f2d; margin: 0;">8</h2>
        <p style="margin: 0.5rem 0 0 0; color: #666;">Analysis Tools</p>
    </div>
    """, unsafe_allow_html=True)

# About the Haney Test Methodology
st.markdown("---")
st.markdown("## 🔬 About the Haney Soil Health Test")

col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("""
    <div class="methodology-card">
    <h3 style="color: #2c5f2d; margin-top: 0;">Revolutionary Soil Analysis</h3>

    The Haney Soil Health Test represents a paradigm shift in agricultural soil testing. Unlike traditional methods
    that treat soil as an inert substrate, the Haney Test measures soil as a <b>living, dynamic ecosystem</b>.

    <h4 style="color: #2c5f2d; margin-top: 1.5rem;">Key Methodology Components:</h4>

    <p><b>🫧 24-Hour CO2-C Respiration:</b><br>
    Measures biological activity by quantifying carbon dioxide released by soil microbes. Higher respiration =
    more active, healthier soil biology.</p>

    <p><b>🧪 H3A Extractant:</b><br>
    Uses weak organic acids that mimic plant root exudates, providing more accurate plant-available nutrient
    measurements than harsh chemical extractants used in traditional testing.</p>

    <p><b>💧 WEOC/WEON (Water-Extractable Organic C/N):</b><br>
    Measures readily available carbon and nitrogen that fuel soil microbial communities - the "food web"
    that drives nutrient cycling.</p>

    <p><b>📊 Integrated Soil Health Score:</b><br>
    Combines biological and chemical data into a single metric that reflects overall soil ecosystem function.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="methodology-card" style="background-color: #e3f2fd;">
    <h3 style="color: #1565c0; margin-top: 0;">Why It Matters</h3>

    <p><b>✅ More Accurate Nutrient Recommendations</b><br>
    Reduces over-application of synthetic fertilizers by accounting for biological nutrient availability</p>

    <p><b>💰 Economic Benefits</b><br>
    Typical nitrogen savings of 30+ lbs/acre translate to significant cost reductions</p>

    <p><b>🌍 Environmental Impact</b><br>
    Lower fertilizer inputs reduce nutrient runoff, leaching, and greenhouse gas emissions</p>

    <p><b>📈 Soil Health Tracking</b><br>
    Biological indicators allow farmers to track improvements from regenerative practices over time</p>
    </div>

    <div class="methodology-card" style="background-color: #f3e5f5; margin-top: 1rem;">
    <h3 style="color: #6a1b9a; margin-top: 0;">🏆 Regen Ag Lab</h3>

    <p>This dashboard is powered by data from <b>Regen Ag Lab</b>, where Dr. Rick Haney serves as
    Chief Scientific Officer.</p>

    <p>Dr. Haney developed this methodology during his career at USDA-ARS, earning multiple national awards
    for technology transfer and innovation. His farmer-first approach bridges cutting-edge soil science
    with practical agricultural decision-making.</p>
    </div>
    """, unsafe_allow_html=True)

# Dashboard Features
st.markdown("---")
st.markdown("## 🎯 Dashboard Features & Navigation")

st.markdown("""
This interactive platform provides comprehensive analysis tools to explore soil health data using the Haney Test methodology.
Launch the main dashboard using the button below to access all features.
""")

st.markdown("<br>", unsafe_allow_html=True)

# Feature Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📈</div>
        <h4 style="color: #2c5f2d;">Overview & Statistics</h4>
        <p>Dataset summary, geographic distribution, and key soil metrics across all samples</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🔬</div>
        <h4 style="color: #2c5f2d;">Soil Health Analysis</h4>
        <p>Haney Soil Health Score distribution, correlations with biological indicators, and rating categories</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🌾</div>
        <h4 style="color: #2c5f2d;">Cover Crop Analysis</h4>
        <p>Impact of cover crop mixes on soil health metrics and nutrient availability</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">💰</div>
        <h4 style="color: #2c5f2d;">Economic Analysis</h4>
        <p>ROI calculator comparing Haney vs Traditional testing with what-if scenarios</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🔗</div>
        <h4 style="color: #2c5f2d;">Correlation Explorer</h4>
        <p>Interactive scatter plots and regression analysis between any two variables</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <h4 style="color: #2c5f2d;">Custom Analysis</h4>
        <p>Flexible data exploration with histograms, box plots, and violin plots</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📚</div>
        <h4 style="color: #2c5f2d;">Data Dictionary</h4>
        <p>Complete reference for all 211+ variables with searchable definitions</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📦</div>
        <h4 style="color: #2c5f2d;">Project Deliverables</h4>
        <p>Download reports, visualizations, and access complete project documentation</p>
    </div>
    """, unsafe_allow_html=True)

# Navigation Guide
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

# How to Use Section
st.markdown("---")
st.markdown("## 📖 How to Use This Dashboard")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### Getting Started

    1. **Launch the Dashboard**: Use the command above to start the Streamlit application
    2. **Select Analysis View**: Use the navbar links to navigate between different analysis pages
    3. **Interact with Charts**: Hover over visualizations to see detailed data points, zoom, and pan
    4. **Download Data**: Export charts and analysis results where available

    ### Key Tips

    - **Dataset Size**: Working with {:,} samples - some visualizations may be sampled for performance
    - **Missing Data**: Not all samples have complete data for every variable
    - **Feedback System**: Use the feedback form to report issues or suggest features
    """.format(n_samples))

with col2:
    st.markdown("""
    ### Technical Requirements

    **Python Packages:**
    - `streamlit` - Dashboard framework
    - `pandas` - Data manipulation
    - `plotly` - Interactive visualizations
    - `uszipcode` - Geographic mapping (optional)

    **System Requirements:**
    - Python 3.8+
    - 4GB+ RAM recommended for large datasets
    - Modern web browser (Chrome, Firefox, Safari, Edge)

    ### Data Sources

    - **Primary Dataset**: combined_soil_data_FULL.csv
    - **Samples**: {:,} soil tests
    - **Variables**: {} measured parameters
    - **Testing Method**: Haney Soil Health Test (Regen Ag Lab)
    """.format(n_samples, n_variables))

# Footer with Regen Ag Lab branding
st.markdown("<hr style='border: none; height: 1px; background-color: #dddddd; margin: 30px 0;'>", unsafe_allow_html=True)

# Convert logo to base64 for embedding
import base64
try:
    with open(LOGO_PATH, "rb") as img_file:
        logo_base64 = base64.b64encode(img_file.read()).decode()
    logo_html = f'<img src="data:image/png;base64,{logo_base64}" style="width: 150px; height: auto;" alt="Regen Ag Lab Logo">'
except:
    logo_html = ""

# Footer with embedded logo
st.markdown(f"""
<div style="background-color: #ffffff; border-top: 4px solid #e40032; padding: 40px 20px; margin-top: 40px;">
    <div style="display: grid; grid-template-columns: 180px 1fr 180px; gap: 30px; max-width: 1240px; margin: 0 auto; align-items: start;">
        <div style="text-align: left;">
            {logo_html}
        </div>
        <div style="text-align: center;">
            <h3 style="color: #53575a; margin-top: 0; font-family: 'Raleway', sans-serif; font-size: 30px; font-weight: 600;">
                Powered by Regen Ag Lab
            </h3>
            <p style="margin: 15px 0; color: #53575a; font-family: 'Raleway', sans-serif; font-size: 17px;">
                <strong>Dr. Rick Haney, Chief Scientific Officer</strong><br>
                Measuring soil as a living system
            </p>
            <p style="margin: 15px 0; font-size: 17px; color: #53575a; font-family: 'Raleway', sans-serif;">
                Visit <a href="https://regenaglab.com/" target="_blank" style="color: #e40032; text-decoration: none; font-weight: 400;">regenaglab.com</a> to learn more about our
                comprehensive soil testing services and regenerative agriculture solutions.
            </p>
        </div>
        <div style="text-align: right;">
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
