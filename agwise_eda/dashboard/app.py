"""
Interactive Agricultural Soil Health EDA Dashboard
Data analysis powered by the Haney Soil Health Test methodology
Built with Streamlit and Plotly (open-source packages)

Developed in partnership with Regen Ag Lab
Date: October 6, 2025
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pathlib import Path
from PIL import Image
from streamlit_option_menu import option_menu
import warnings
warnings.filterwarnings('ignore')

# For ZIP code geocoding
try:
    from uszipcode import SearchEngine
    USZIPCODE_AVAILABLE = True
except ImportError:
    USZIPCODE_AVAILABLE = False

# Page configuration
st.set_page_config(
    page_title="Haney Soil Health Analysis Dashboard",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"  # Collapse sidebar since we're using top nav
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
        --color-green: #81d742;
        --color-border-light: #dddddd;
        --color-border-medium: #eaeaea;
        --font-family: 'Raleway', sans-serif;
        --border-radius: 5px;
    }

    /* Override Streamlit defaults - background and fonts */
    .stApp {
        background-color: #f5f5f5 !important;
    }

    .main .block-container {
        background-color: #f5f5f5 !important;
    }

    /* Hide sidebar completely since we're using top navigation */
    [data-testid="stSidebar"] {
        display: none !important;
    }

    /* Hide sidebar toggle button */
    button[kind="header"] {
        display: none !important;
    }

    /* Hide Streamlit's default header */
    header[data-testid="stHeader"] {
        display: none !important;
    }

    .stApp > header {
        display: none !important;
    }

    /* Adjust main content area to use full width */
    .main {
        margin-left: 0 !important;
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

    h1 { font-size: 48px !important; }
    h2 { font-size: 42px !important; }
    h3 { font-size: 30px !important; }
    h4 { font-size: 20px !important; }

    /* Main header */
    .main-header {
        font-size: 36px;
        color: #e40032;
        font-weight: 600;
        text-align: center;
        padding: 1rem 0;
        font-family: 'Raleway', sans-serif;
    }

    /* Metric cards - Regen brand style */
    .regen-metric {
        background-color: #ffffff;
        padding: 25px 20px;
        border-radius: 5px;
        border: 2px solid #eaeaea;
        text-align: center;
        transition: all 0.3s ease;
    }

    .regen-metric:hover {
        border-color: #e40032;
    }

    .regen-metric-value {
        font-size: 42px;
        font-weight: 600;
        color: #e40032;
        margin: 0;
        font-family: 'Raleway', sans-serif;
        line-height: 1.2;
    }

    .regen-metric-label {
        font-size: 17px;
        font-weight: 400;
        color: #53575a;
        margin: 10px 0 0 0;
        font-family: 'Raleway', sans-serif;
    }

    /* Info box */
    .info-box {
        background-color: #ffffff;
        padding: 20px 25px;
        border-radius: 5px;
        border: 1px solid #eaeaea;
        margin: 1rem 0;
        color: #53575a;
        font-family: 'Raleway', sans-serif;
        font-size: 17px;
    }

    /* Feedback box */
    .feedback-box {
        background-color: #ffffff;
        padding: 20px 25px;
        border-radius: 5px;
        border-left: 4px solid #e40032;
        margin: 1rem 0;
        color: #53575a;
        font-family: 'Raleway', sans-serif;
    }

    /* Service Cards */
    .regen-card {
        background-color: #ffffff;
        padding: 30px 25px;
        border-radius: 5px;
        border: 1px solid #eaeaea;
        text-align: center;
        height: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }

    .regen-card:hover {
        border-color: #e40032;
        box-shadow: 0 4px 8px rgba(228, 0, 50, 0.15);
        transform: translateY(-3px);
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
        text-align: center;
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

    /* Table styling with gradient header matching Regen Ag Lab */
    .dataframe {
        font-family: 'Raleway', sans-serif !important;
        border-collapse: collapse !important;
        width: 100% !important;
    }

    .dataframe thead tr {
        background: linear-gradient(to right, #eb4065, #e40032) !important;
    }

    .dataframe thead th {
        color: #ffffff !important;
        font-size: 18px !important;
        font-weight: 700 !important;
        padding: 15px !important;
        text-align: center !important;
        border: 1px solid #e40032 !important;
        font-family: 'Raleway', sans-serif !important;
    }

    .dataframe tbody td {
        background: #EEEEEE !important;
        border: 1px solid #AAAAAA !important;
        padding: 10px 15px !important;
        text-align: center !important;
        font-size: 17px !important;
        font-weight: 400 !important;
        color: #53575a !important;
        line-height: 1.5 !important;
        font-family: 'Raleway', sans-serif !important;
    }

    .dataframe tbody tr:nth-child(even) td {
        background: #ffffff !important;
    }

    /* Streamlit table styling - multiple selectors for compatibility */
    table, [data-testid="stTable"] table, .stDataFrame table {
        font-family: 'Raleway', sans-serif !important;
        border-collapse: collapse !important;
    }

    thead, [data-testid="stTable"] thead, .stDataFrame thead {
        background: linear-gradient(to right, #eb4065, #e40032) !important;
    }

    th, [data-testid="stTable"] th, .stDataFrame th {
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 18px !important;
        padding: 15px !important;
        border: 1px solid #e40032 !important;
        background: linear-gradient(to right, #eb4065, #e40032) !important;
    }

    td, [data-testid="stTable"] td, .stDataFrame td {
        background: #EEEEEE !important;
        border: 1px solid #AAAAAA !important;
        padding: 10px 15px !important;
        text-align: center !important;
        font-size: 17px !important;
        font-weight: 400 !important;
        color: #53575a !important;
        font-family: 'Raleway', sans-serif !important;
    }

    tr:nth-child(even) td {
        background: #ffffff !important;
    }

    /* Streamlit dataframe container styling */
    [data-testid="stDataFrame"] {
        font-family: 'Raleway', sans-serif !important;
    }

    [data-testid="stDataFrame"] th {
        background: linear-gradient(to right, #eb4065, #e40032) !important;
        color: #ffffff !important;
    }

    /* Section headers with red accent */
    .section-header {
        color: #e40032 !important;
        font-family: 'Raleway', sans-serif !important;
        font-weight: 600 !important;
        border-bottom: 3px solid #e40032;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }

    /* Divider with red accent */
    .regen-divider {
        height: 2px;
        background: linear-gradient(to right, transparent, #e40032, transparent);
        border: none;
        margin: 30px 0;
    }

    /* Streamlit metric styling - use dark gray for positive association */
    [data-testid="stMetricValue"] {
        color: #53575a !important;
        font-family: 'Raleway', sans-serif !important;
        font-weight: 600 !important;
        font-size: 32px !important;
    }

    [data-testid="stMetricLabel"] {
        color: #53575a !important;
        font-family: 'Raleway', sans-serif !important;
        font-size: 15px !important;
    }

    /* Streamlit headers */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #53575a !important;
    }

    /* Plotly chart backgrounds and styling */
    .js-plotly-plot .plotly {
        background-color: #f5f5f5 !important;
    }

    .js-plotly-plot .plotly .bg {
        fill: #f5f5f5 !important;
    }

    .js-plotly-plot .plotly .gridlayer .grid {
        stroke: #dddddd !important;
    }

    /* Plotly text colors */
    .js-plotly-plot .plotly text {
        fill: #53575a !important;
        font-family: 'Raleway', sans-serif !important;
    }

    .js-plotly-plot .plotly .xtick text,
    .js-plotly-plot .plotly .ytick text {
        fill: #53575a !important;
    }

    .js-plotly-plot .plotly .g-gtitle text,
    .js-plotly-plot .plotly .g-xtitle text,
    .js-plotly-plot .plotly .g-ytitle text {
        fill: #53575a !important;
        font-weight: 600 !important;
    }
</style>
""", unsafe_allow_html=True)

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DASHBOARD_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / 'data' / 'processed' / 'combined_soil_data_FULL.csv'
LOGO_PATH = DASHBOARD_DIR / 'assets' / 'regen_ag_lab_logo.png'
FEEDBACK_DIR = BASE_DIR / 'feedback'
FEEDBACK_FILE = FEEDBACK_DIR / 'user_feedback.csv'
FEEDBACK_UPLOADS = FEEDBACK_DIR / 'uploads'

# Ensure feedback directories exist
FEEDBACK_DIR.mkdir(parents=True, exist_ok=True)
FEEDBACK_UPLOADS.mkdir(parents=True, exist_ok=True)

# Set default Plotly template for light gray backgrounds
import plotly.io as pio

# Create custom Regen Ag Lab template
regen_template = go.layout.Template()
regen_template.layout = go.Layout(
    plot_bgcolor='#f5f5f5',
    paper_bgcolor='#f5f5f5',
    font=dict(
        family='Raleway, sans-serif',
        size=14,
        color='#53575a'
    ),
    title_font=dict(
        family='Raleway, sans-serif',
        size=18,
        color='#53575a'
    ),
    xaxis=dict(
        gridcolor='#dddddd',
        tickfont=dict(color='#53575a', family='Raleway, sans-serif'),
        title=dict(font=dict(color='#53575a', size=15, family='Raleway, sans-serif')),
        linecolor='#dddddd',
        zerolinecolor='#dddddd'
    ),
    yaxis=dict(
        gridcolor='#dddddd',
        tickfont=dict(color='#53575a', family='Raleway, sans-serif'),
        title=dict(font=dict(color='#53575a', size=15, family='Raleway, sans-serif')),
        linecolor='#dddddd',
        zerolinecolor='#dddddd'
    ),
    colorway=['#e40032', '#53575a', '#81d742', '#eb4065', '#464646']
)

# Register and set as default
pio.templates['regen'] = regen_template
pio.templates.default = 'regen'

# Custom Plotly layout defaults
def apply_regen_style(fig):
    """Apply Regen Ag Lab styling to Plotly figures"""
    fig.update_layout(
        template='regen',
        plot_bgcolor='#f5f5f5',
        paper_bgcolor='#f5f5f5',
        font=dict(
            family='Raleway, sans-serif',
            size=14,
            color='#53575a'
        ),
        title_font=dict(
            family='Raleway, sans-serif',
            size=18,
            color='#53575a'
        )
    )
    fig.update_xaxes(
        gridcolor='#dddddd',
        tickfont=dict(color='#53575a', family='Raleway, sans-serif'),
        title_font=dict(color='#53575a', size=15, family='Raleway, sans-serif'),
        linecolor='#dddddd',
        zerolinecolor='#dddddd'
    )
    fig.update_yaxes(
        gridcolor='#dddddd',
        tickfont=dict(color='#53575a', family='Raleway, sans-serif'),
        title_font=dict(color='#53575a', size=15, family='Raleway, sans-serif'),
        linecolor='#dddddd',
        zerolinecolor='#dddddd'
    )
    return fig

# Cache data loading
@st.cache_data
def load_data():
    """Load and cache the dataset"""
    df = pd.read_csv(DATA_FILE)
    return df

# Feedback system functions
def save_feedback(page, feedback_type, message, uploaded_file=None):
    """Save user feedback to CSV file"""
    import datetime

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Handle file upload
    file_path = None
    if uploaded_file is not None:
        # Save uploaded file
        file_ext = uploaded_file.name.split('.')[-1]
        file_path = FEEDBACK_UPLOADS / f"feedback_{timestamp.replace(':', '-').replace(' ', '_')}.{file_ext}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        file_path = str(file_path.relative_to(BASE_DIR))

    # Prepare feedback entry
    feedback_entry = {
        'timestamp': timestamp,
        'page': page,
        'type': feedback_type,
        'message': message,
        'file_attachment': file_path or 'None'
    }

    # Append to CSV
    feedback_df = pd.DataFrame([feedback_entry])

    if FEEDBACK_FILE.exists():
        # Append to existing file
        feedback_df.to_csv(FEEDBACK_FILE, mode='a', header=False, index=False)
    else:
        # Create new file with header
        feedback_df.to_csv(FEEDBACK_FILE, mode='w', header=True, index=False)

    return True

# Load data
try:
    data = load_data()
    data_loaded = True
except Exception as e:
    st.error(f"Error loading data: {e}")
    data_loaded = False

if data_loaded:
    # Top Navigation Bar with Dropdown - Must be at the very top
    st.markdown("""
    <style>
        /* Custom top navigation bar */
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

    <div class="top-nav">
        <div class="nav-container">
            <div class="nav-logo">Haney Soil AI</div>
            <ul class="nav-menu">
                <li class="nav-item"><a href="Home" target="_parent" class="nav-link">Home</a></li>
                <li class="nav-item dropdown">
                    <span class="nav-link">Analysis <span class="dropdown-arrow">▼</span></span>
                    <div class="dropdown-content">
                        <a href="?view=overview" target="_parent">📈 Overview & Statistics</a>
                        <a href="?view=soil_health" target="_parent">🔬 Soil Health Analysis</a>
                        <a href="?view=cover_crop" target="_parent">🌾 Cover Crop Analysis</a>
                        <a href="?view=economic" target="_parent">💰 Economic Analysis</a>
                        <a href="?view=correlation" target="_parent">🔗 Correlation Explorer</a>
                        <a href="?view=custom" target="_parent">📊 Custom Analysis</a>
                        <a href="?view=dictionary" target="_parent">📚 Data Dictionary</a>
                        <a href="?view=deliverables" target="_parent">📦 Project Deliverables</a>
                    </div>
                </li>
                <li class="nav-item"><a href="Economic_Analysis" target="_parent" class="nav-link">Economic Analysis</a></li>
                <li class="nav-item"><a href="Feedback" target="_parent" class="nav-link">Feedback</a></li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Get query parameters for view selection
    query_params = st.query_params
    view = query_params.get("view", "overview")

    # Map view to page name
    view_mapping = {
        "overview": "📈 Overview & Statistics",
        "soil_health": "🔬 Soil Health Analysis",
        "cover_crop": "🌾 Cover Crop Analysis",
        "economic": "💰 Economic Analysis",
        "correlation": "🔗 Correlation Explorer",
        "custom": "📊 Custom Analysis",
        "dictionary": "📚 Data Dictionary",
        "deliverables": "📦 Project Deliverables"
    }

    page = view_mapping.get(view, "📈 Overview & Statistics")

    # Header - Regen Ag Lab brand styling
    st.markdown("""
    <div style="text-align: center; padding: 1rem 1rem 1rem 1rem;">
        <h2 style="color: #53575a; margin: 0; font-size: 30px; font-weight: 600; font-family: 'Raleway', sans-serif;">
            Agricultural Soil Health Analysis Dashboard
        </h2>
        <p style="color: #53575a; margin: 0.5rem 0 0 0; font-size: 17px; font-family: 'Raleway', sans-serif;">
            Powered by the Haney Soil Health Test Methodology
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Count batches dynamically
    n_batches = data['_source_batch'].nunique() if '_source_batch' in data.columns else 'Unknown'

    st.markdown(f"""
    <div class="info-box">
    <b>Dataset Overview:</b> {len(data):,} samples | {len(data.columns)} variables |
    {n_batches} batches | Interactive analysis powered by Haney Test data
    </div>
    """, unsafe_allow_html=True)

    # ==================================================================
    # PAGE 1: OVERVIEW & STATISTICS
    # ==================================================================
    if page == "📈 Overview & Statistics":
        st.markdown('<h2 class="section-header">📈 Dataset Overview & Key Statistics</h2>', unsafe_allow_html=True)

        # Top metrics
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Total Samples", f"{len(data):,}",
                     delta=f"{len(data):,} samples")
        with col2:
            unique = len(data) - data.duplicated().sum()
            dup_pct = (data.duplicated().sum() / len(data) * 100)
            st.metric("Unique Samples", f"{unique:,}",
                     delta=f"-{dup_pct:.1f}% duplicates", delta_color="inverse")
        with col3:
            st.metric("Variables", len(data.columns),
                     delta=f"{len(data.columns)} total")
        with col4:
            batch_col = '_source_batch'
            if batch_col in data.columns:
                n_batches = data[batch_col].nunique()
                st.metric("Data Batches", n_batches)

        st.markdown("---")

        # Batch comparison
        st.markdown('<h3 style="color: #e40032; font-family: Raleway, sans-serif; font-weight: 600;">📦 Batch Distribution</h3>', unsafe_allow_html=True)
        if '_source_batch' in data.columns:
            batch_counts = data['_source_batch'].value_counts().sort_index()

            fig = go.Figure(data=[
                go.Bar(x=batch_counts.index, y=batch_counts.values,
                      marker_color='#e40032')
            ])
            fig.update_layout(
                title="Samples by Batch",
                xaxis_title="Batch",
                yaxis_title="Number of Samples",
                height=400
            )
            fig = apply_regen_style(fig)
            st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")

        # Geographic Distribution
        st.markdown('<h3 style="color: #e40032; font-family: Raleway, sans-serif; font-weight: 600;">🗺️ Geographic Distribution of Samples</h3>', unsafe_allow_html=True)

        if 'Zip' in data.columns:
            zip_data = data['Zip'].dropna()

            if len(zip_data) > 0:
                # Clean ZIP codes: handle both string and numeric formats
                def clean_zip(z):
                    try:
                        z_str = str(z)
                        if '.' in z_str:
                            z_str = str(int(float(z_str)))
                        return z_str.zfill(5) if z_str.isdigit() and len(z_str) <= 5 else None
                    except:
                        return None

                zip_cleaned = zip_data.apply(clean_zip).dropna()

                # Count samples by ZIP code
                zip_counts = zip_cleaned.value_counts().reset_index()
                zip_counts.columns = ['zip', 'count']

                # Display summary stats
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Samples with ZIP", f"{len(zip_cleaned):,}")
                with col2:
                    st.metric("Unique ZIP Codes", f"{len(zip_counts):,}")
                with col3:
                    st.metric("Most Common ZIP", str(zip_counts.iloc[0]['zip']))
                with col4:
                    st.metric("Samples in Top ZIP", f"{zip_counts.iloc[0]['count']:,}")

                # Create map visualization
                if USZIPCODE_AVAILABLE:
                    st.info("💡 Geocoding ZIP codes for map visualization... This may take a moment on first load.")

                    # Cache the geocoding result
                    @st.cache_data
                    def geocode_zips(zip_counts_df):
                        search = SearchEngine()
                        geocoded = []

                        for idx, row in zip_counts_df.head(200).iterrows():  # Limit to top 200 for performance
                            try:
                                # Handle both string and numeric ZIP codes
                                zip_raw = row['zip']
                                if pd.isna(zip_raw):
                                    continue

                                # Convert to string, handle float format
                                zip_str = str(zip_raw)
                                if '.' in zip_str:
                                    zip_str = str(int(float(zip_str)))

                                # Ensure 5-digit format
                                zip_str = zip_str.zfill(5)

                                # Only process valid 5-digit US ZIP codes
                                if len(zip_str) == 5 and zip_str.isdigit():
                                    result = search.by_zipcode(zip_str)
                                    if result and result.lat and result.lng:
                                        geocoded.append({
                                            'zip': zip_str,
                                            'count': row['count'],
                                            'lat': result.lat,
                                            'lng': result.lng,
                                            'city': result.major_city or 'Unknown',
                                            'state': result.state or 'Unknown'
                                        })
                            except (ValueError, TypeError) as e:
                                # Skip invalid ZIP codes
                                continue

                        return pd.DataFrame(geocoded)

                    try:
                        geo_data = geocode_zips(zip_counts)

                        if len(geo_data) > 0:
                            # Create scatter map
                            fig = px.scatter_geo(
                                geo_data,
                                lat='lat',
                                lon='lng',
                                size='count',
                                hover_name='zip',
                                hover_data={
                                    'city': True,
                                    'state': True,
                                    'count': True,
                                    'lat': ':.3f',
                                    'lng': ':.3f'
                                },
                                title=f'Sample Distribution Across ZIP Codes (Top {len(geo_data)} ZIPs)',
                                size_max=40,
                                color='count',
                                color_continuous_scale='Greens'
                            )

                            fig.update_geos(
                                scope='usa',
                                showcountries=True,
                                showsubunits=True,
                                showlakes=True
                            )

                            fig.update_layout(
                                height=600,
                                geo=dict(
                                    bgcolor='rgba(0,0,0,0)',
                                    lakecolor='lightblue',
                                    landcolor='white'
                                )
                            )

                            fig = apply_regen_style(fig)
                            st.plotly_chart(fig, use_container_width=True)

                            # Show top 10 locations
                            st.subheader("📍 Top 10 Sample Locations")
                            top_10 = geo_data.nlargest(10, 'count')[['zip', 'city', 'state', 'count']]
                            top_10.columns = ['ZIP Code', 'City', 'State', 'Sample Count']

                            # Create HTML table with Regen Ag Lab styling
                            html_table = '<table class="regen-table" style="width: 100%; border-collapse: collapse; font-family: Raleway, sans-serif;">'
                            html_table += '<thead><tr>'
                            for col in top_10.columns:
                                html_table += f'<th style="background: linear-gradient(to right, #eb4065, #e40032); color: #ffffff; font-size: 18px; font-weight: 700; padding: 15px; text-align: center; border: 1px solid #e40032;">{col}</th>'
                            html_table += '</tr></thead><tbody>'

                            for idx, row in top_10.iterrows():
                                bg_color = '#ffffff' if idx % 2 == 0 else '#EEEEEE'
                                html_table += '<tr>'
                                for val in row:
                                    html_table += f'<td style="background: {bg_color}; border: 1px solid #AAAAAA; padding: 10px 15px; text-align: center; font-size: 17px; color: #53575a;">{val}</td>'
                                html_table += '</tr>'

                            html_table += '</tbody></table>'
                            st.markdown(html_table, unsafe_allow_html=True)
                        else:
                            st.warning("Unable to geocode ZIP codes. Showing distribution table instead.")
                            # Fallback to table
                            st.dataframe(zip_counts.head(20), use_container_width=True)

                    except Exception as e:
                        st.warning(f"Map geocoding encountered an issue: {e}. Showing distribution table.")
                        st.dataframe(zip_counts.head(20), use_container_width=True)

                else:
                    # Fallback if uszipcode not available
                    st.warning("⚠️ Geographic mapping requires the `uszipcode` package. Install it with: `pip install uszipcode`")

                    st.subheader("📊 Top 20 ZIP Codes by Sample Count")
                    top_20 = zip_counts.head(20)

                    fig = go.Figure(data=[
                        go.Bar(x=top_20['zip'].astype(str), y=top_20['count'],
                              marker_color='#2c5f2d')
                    ])
                    fig.update_layout(
                        title="Sample Distribution by ZIP Code (Top 20)",
                        xaxis_title="ZIP Code",
                        yaxis_title="Number of Samples",
                        height=500
                    )
                    fig.update_xaxes(tickangle=45)
                    fig = apply_regen_style(fig)
                    st.plotly_chart(fig, use_container_width=True)

                    st.dataframe(zip_counts.head(20), use_container_width=True)
        else:
            st.info("ZIP code data not available in the dataset.")

        st.markdown("---")

        # Key metrics statistics
        st.markdown('<h3 style="color: #e40032; font-family: Raleway, sans-serif; font-weight: 600;">📊 Key Soil Metrics Statistics</h3>', unsafe_allow_html=True)

        key_metrics = ['1:1 Soil pH', 'Organic Matter', 'CO2-C',
                      'Soil Health Calculation', 'H3A Nitrate']
        available_metrics = [col for col in key_metrics if col in data.columns]

        if available_metrics:
            stats_data = []
            for col in available_metrics:
                values = pd.to_numeric(data[col], errors='coerce').dropna()
                if len(values) > 0:
                    stats_data.append({
                        'Metric': col,
                        'Count': f"{len(values):,}",
                        'Mean': f"{values.mean():.2f}",
                        'Median': f"{values.median():.2f}",
                        'Std Dev': f"{values.std():.2f}",
                        'Min': f"{values.min():.2f}",
                        'Max': f"{values.max():.2f}"
                    })

            stats_df = pd.DataFrame(stats_data)

            # Create HTML table with Regen Ag Lab styling
            html_table = '<table class="regen-table" style="width: 100%; border-collapse: collapse; margin: 20px 0; font-family: Raleway, sans-serif;">'
            html_table += '<thead><tr>'
            for col in stats_df.columns:
                html_table += f'<th style="background: linear-gradient(to right, #eb4065, #e40032); color: #ffffff; font-size: 18px; font-weight: 700; padding: 15px; text-align: center; border: 1px solid #e40032;">{col}</th>'
            html_table += '</tr></thead><tbody>'

            for idx, row in stats_df.iterrows():
                bg_color = '#ffffff' if idx % 2 == 0 else '#EEEEEE'
                html_table += '<tr>'
                for val in row:
                    html_table += f'<td style="background: {bg_color}; border: 1px solid #AAAAAA; padding: 10px 15px; text-align: center; font-size: 17px; color: #53575a; line-height: 1.5;">{val}</td>'
                html_table += '</tr>'

            html_table += '</tbody></table>'
            st.markdown(html_table, unsafe_allow_html=True)

    # ==================================================================
    # PAGE 2: SOIL HEALTH ANALYSIS
    # ==================================================================
    elif page == "🔬 Soil Health Analysis":
        st.markdown('<h2 class="section-header">🔬 Haney Soil Health Score Analysis</h2>', unsafe_allow_html=True)

        st.markdown("""
        <div class="info-box">
        <b>About the Haney Soil Health Score:</b> This integrated metric combines biological activity (24-hr CO2-C respiration)
        with chemical analysis using the H3A extractant. Unlike traditional testing, the Haney method measures soil as a
        living ecosystem, providing more accurate plant-available nutrient estimates.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        health_col = 'Soil Health Calculation' if 'Soil Health Calculation' in data.columns else 'Soil Health Score'

        if health_col in data.columns:
            health_data = pd.to_numeric(data[health_col], errors='coerce').dropna()

            # Key metrics
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.metric("Mean Score", f"{health_data.mean():.2f}")
            with col2:
                st.metric("Median Score", f"{health_data.median():.2f}")
            with col3:
                st.metric("Std Dev", f"{health_data.std():.2f}")
            with col4:
                st.metric("Min", f"{health_data.min():.2f}")
            with col5:
                st.metric("Max", f"{health_data.max():.2f}")

            st.markdown("---")

            # Distribution plot
            col1, col2 = st.columns([2, 1])

            with col1:
                fig = go.Figure()
                fig.add_trace(go.Histogram(
                    x=health_data,
                    nbinsx=50,
                    name='Distribution',
                    marker_color='#2c5f2d',
                    opacity=0.7
                ))
                fig.add_vline(x=health_data.mean(), line_dash="dash",
                             line_color="red", annotation_text="Mean")
                fig.add_vline(x=health_data.median(), line_dash="dash",
                             line_color="blue", annotation_text="Median")
                fig.update_layout(
                    title=f"{health_col} Distribution",
                    xaxis_title=health_col,
                    yaxis_title="Frequency",
                    height=500
                )
                fig = apply_regen_style(fig)
                st.plotly_chart(fig, use_container_width=True)

            with col2:
                # Categories
                st.subheader("Score Categories")
                bins = [0, 2, 5, 10, 150]
                labels = ['Poor (0-2)', 'Fair (2-5)', 'Good (5-10)', 'Excellent (10+)']
                categories = pd.cut(health_data, bins=bins, labels=labels)
                cat_counts = categories.value_counts().sort_index()

                fig = go.Figure(data=[
                    go.Pie(labels=cat_counts.index, values=cat_counts.values,
                          marker_colors=['#d32f2f', '#ff9800', '#ffc107', '#4caf50'])
                ])
                fig.update_layout(height=400, title="Health Categories")
                fig = apply_regen_style(fig)
                st.plotly_chart(fig, use_container_width=True)

            # Factors analysis
            st.markdown('<h3 style="color: #e40032; font-family: Raleway, sans-serif; font-weight: 600;">🎯 Top Factors Correlated with Soil Health</h3>', unsafe_allow_html=True)

            analysis_cols = ['CO2-C', 'Organic Matter', '1:1 Soil pH',
                           'H3A ICAP Potassium', 'H3A ICAP Calcium']
            available_analysis = [col for col in analysis_cols
                                if col in data.columns and data[col].notna().sum() > 100]

            if available_analysis:
                correlations = []
                for col in available_analysis:
                    temp_df = data[[health_col, col]].apply(pd.to_numeric, errors='coerce').dropna()
                    if len(temp_df) > 50:
                        corr = temp_df[health_col].corr(temp_df[col])
                        correlations.append({'Factor': col, 'Correlation': corr})

                if correlations:
                    corr_df = pd.DataFrame(correlations).sort_values('Correlation', ascending=False)

                    fig = go.Figure(data=[
                        go.Bar(x=corr_df['Factor'], y=corr_df['Correlation'],
                              marker_color=['#2c5f2d' if x > 0 else '#d32f2f'
                                          for x in corr_df['Correlation']])
                    ])
                    fig.update_layout(
                        title="Correlation with Soil Health",
                        xaxis_title="Factor",
                        yaxis_title="Correlation Coefficient",
                        height=400
                    )
                    fig = apply_regen_style(fig)
                    st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Soil Health Score data not available in dataset.")

    # ==================================================================
    # PAGE 3: COVER CROP ANALYSIS
    # ==================================================================
    elif page == "🌾 Cover Crop Analysis":
        st.markdown('<h2 class="section-header">🌾 Cover Crop Mix Analysis</h2>', unsafe_allow_html=True)

        cover_cols = ['Cover Crop Mix', 'Cover crop mix']
        cover_col = None
        for col in cover_cols:
            if col in data.columns and data[col].notna().sum() > 50:
                cover_col = col
                break

        if cover_col:
            cover_data = data[cover_col].dropna()

            # Distribution
            st.subheader("📊 Cover Crop Mix Distribution")
            value_counts = cover_data.value_counts()

            fig = go.Figure(data=[
                go.Bar(x=value_counts.index, y=value_counts.values,
                      marker_color='#2c5f2d')
            ])
            fig.update_layout(
                title=f"Distribution of {cover_col}",
                xaxis_title="Cover Crop Mix",
                yaxis_title="Count",
                height=500
            )
            fig.update_xaxes(tickangle=45)
            fig = apply_regen_style(fig)
            st.plotly_chart(fig, use_container_width=True)

            # Health by cover crop
            health_col = 'Soil Health Calculation' if 'Soil Health Calculation' in data.columns else 'Soil Health Score'

            if health_col in data.columns:
                st.subheader("🌱 Soil Health by Cover Crop Mix")

                cover_health = data[[cover_col, health_col]].copy()
                cover_health[health_col] = pd.to_numeric(cover_health[health_col], errors='coerce')
                cover_health = cover_health.dropna()

                if len(cover_health) > 0:
                    # Box plot
                    fig = go.Figure()

                    for mix in sorted(cover_health[cover_col].unique()):
                        mix_data = cover_health[cover_health[cover_col] == mix][health_col]
                        fig.add_trace(go.Box(y=mix_data, name=mix))

                    fig.update_layout(
                        title=f"{health_col} by Cover Crop Mix",
                        yaxis_title=health_col,
                        xaxis_title="Cover Crop Mix",
                        height=500,
                        showlegend=False
                    )
                    fig.update_xaxes(tickangle=45)
                    fig = apply_regen_style(fig)
                    st.plotly_chart(fig, use_container_width=True)

                    # Summary statistics
                    summary = cover_health.groupby(cover_col)[health_col].agg([
                        'count', 'mean', 'median', 'std', 'min', 'max'
                    ]).round(2).sort_values('mean', ascending=False)

                    st.subheader("📈 Summary Statistics by Cover Crop")

                    # Convert summary to dataframe with proper formatting
                    summary_df = summary.reset_index()
                    summary_df.columns = ['Cover Crop Mix', 'Count', 'Mean', 'Median', 'Std Dev', 'Min', 'Max']

                    # Create HTML table with Regen Ag Lab styling
                    html_table = '<table class="regen-table" style="width: 100%; border-collapse: collapse; margin: 20px 0; font-family: Raleway, sans-serif;">'
                    html_table += '<thead><tr>'
                    for col in summary_df.columns:
                        html_table += f'<th style="background: linear-gradient(to right, #eb4065, #e40032); color: #ffffff; font-size: 18px; font-weight: 700; padding: 15px; text-align: center; border: 1px solid #e40032;">{col}</th>'
                    html_table += '</tr></thead><tbody>'

                    for idx, row in summary_df.iterrows():
                        bg_color = '#ffffff' if idx % 2 == 0 else '#EEEEEE'
                        html_table += '<tr>'
                        for val in row:
                            html_table += f'<td style="background: {bg_color}; border: 1px solid #AAAAAA; padding: 10px 15px; text-align: center; font-size: 17px; color: #53575a; line-height: 1.5;">{val}</td>'
                        html_table += '</tr>'

                    html_table += '</tbody></table>'
                    st.markdown(html_table, unsafe_allow_html=True)
        else:
            st.warning("Cover Crop Mix data not available in dataset.")

    # ==================================================================
    # PAGE 4: ECONOMIC ANALYSIS
    # ==================================================================
    elif page == "💰 Economic Analysis":
        st.markdown('<h2 class="section-header">💰 Traditional vs Haney Test Economic Analysis</h2>', unsafe_allow_html=True)

        trad_col = 'Traditional N'
        haney_col = 'Haney Test N'

        if trad_col in data.columns and haney_col in data.columns:
            comparison = data[[trad_col, haney_col]].apply(pd.to_numeric, errors='coerce').dropna()

            if len(comparison) > 0:
                # Key metrics
                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    st.metric("Sample Size", f"{len(comparison):,}")
                with col2:
                    st.metric("Traditional Mean", f"{comparison[trad_col].mean():.2f} lbs/A")
                with col3:
                    st.metric("Haney Mean", f"{comparison[haney_col].mean():.2f} lbs/A")
                with col4:
                    diff = comparison[haney_col].mean() - comparison[trad_col].mean()
                    st.metric("Mean Difference", f"{diff:.2f} lbs/A",
                             delta=f"+{diff:.1f}")

                st.markdown("---")

                # Scatter plot with 1:1 line
                col1, col2 = st.columns(2)

                with col1:
                    # Sample for performance
                    if len(comparison) > 2000:
                        plot_data = comparison.sample(2000, random_state=42)
                    else:
                        plot_data = comparison

                    fig = go.Figure()
                    fig.add_trace(go.Scatter(
                        x=plot_data[trad_col],
                        y=plot_data[haney_col],
                        mode='markers',
                        marker=dict(color='#2c5f2d', size=5, opacity=0.5),
                        name='Samples'
                    ))

                    # 1:1 line
                    max_val = max(plot_data[trad_col].max(), plot_data[haney_col].max())
                    fig.add_trace(go.Scatter(
                        x=[0, max_val], y=[0, max_val],
                        mode='lines',
                        line=dict(color='red', dash='dash'),
                        name='1:1 Line'
                    ))

                    fig.update_layout(
                        title="Traditional vs Haney N Recommendations",
                        xaxis_title=f"{trad_col} (lbs/A)",
                        yaxis_title=f"{haney_col} (lbs/A)",
                        height=500
                    )
                    fig = apply_regen_style(fig)
                    st.plotly_chart(fig, use_container_width=True)

                with col2:
                    # Box plot comparison
                    fig = go.Figure()
                    fig.add_trace(go.Box(y=comparison[trad_col], name='Traditional',
                                        marker_color='#ffc107'))
                    fig.add_trace(go.Box(y=comparison[haney_col], name='Haney',
                                        marker_color='#2c5f2d'))

                    fig.update_layout(
                        title="Distribution Comparison",
                        yaxis_title="N Recommendation (lbs/A)",
                        height=500
                    )
                    fig = apply_regen_style(fig)
                    st.plotly_chart(fig, use_container_width=True)

                # Economic impact
                st.subheader("💵 Economic Impact Calculation")

                n_cost = st.slider("Nitrogen Cost ($/lb)", 0.5, 2.0, 1.0, 0.1)

                difference = comparison[haney_col] - comparison[trad_col]
                cost_savings = difference * n_cost

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Avg Savings/Sample", f"${cost_savings.mean():.2f}")
                with col2:
                    st.metric("Median Savings/Sample", f"${cost_savings.median():.2f}")
                with col3:
                    st.metric("Total Dataset Savings", f"${cost_savings.sum():,.2f}")
        else:
            st.warning("Traditional vs Haney test data not available.")

    # ==================================================================
    # PAGE 5: CORRELATION EXPLORER
    # ==================================================================
    elif page == "🔗 Correlation Explorer":
        st.markdown('<h2 class="section-header">🔗 Correlation Explorer</h2>', unsafe_allow_html=True)

        # Select variables for correlation
        numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist()
        # Filter to columns with sufficient data
        valid_cols = [col for col in numeric_cols
                     if data[col].notna().sum() > 100 and col not in ['_source_file', '_source_batch']]

        st.subheader("Select Variables to Analyze")

        col1, col2 = st.columns(2)

        with col1:
            var1 = st.selectbox("Variable 1:", valid_cols,
                               index=valid_cols.index('Soil Health Calculation')
                               if 'Soil Health Calculation' in valid_cols else 0)

        with col2:
            var2 = st.selectbox("Variable 2:", valid_cols,
                               index=valid_cols.index('CO2-C')
                               if 'CO2-C' in valid_cols else 1)

        if var1 and var2:
            corr_data = data[[var1, var2]].apply(pd.to_numeric, errors='coerce').dropna()

            if len(corr_data) > 0:
                correlation = corr_data[var1].corr(corr_data[var2])

                # Display correlation
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Sample Size", f"{len(corr_data):,}")
                with col2:
                    corr_color = "normal" if abs(correlation) < 0.5 else "inverse" if correlation < 0 else "normal"
                    st.metric("Correlation (r)", f"{correlation:.3f}")
                with col3:
                    strength = "Very Strong" if abs(correlation) > 0.7 else \
                              "Strong" if abs(correlation) > 0.5 else \
                              "Moderate" if abs(correlation) > 0.3 else "Weak"
                    st.metric("Strength", strength)

                # Scatter plot
                # Sample for performance
                if len(corr_data) > 2000:
                    plot_data = corr_data.sample(2000, random_state=42)
                else:
                    plot_data = corr_data

                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=plot_data[var1],
                    y=plot_data[var2],
                    mode='markers',
                    marker=dict(
                        color=plot_data[var1],
                        colorscale='Viridis',
                        size=5,
                        opacity=0.6,
                        showscale=True
                    ),
                    name='Data'
                ))

                # Add regression line
                z = np.polyfit(plot_data[var1], plot_data[var2], 1)
                p = np.poly1d(z)
                x_line = np.linspace(plot_data[var1].min(), plot_data[var1].max(), 100)
                fig.add_trace(go.Scatter(
                    x=x_line, y=p(x_line),
                    mode='lines',
                    line=dict(color='red', width=2),
                    name='Regression Line'
                ))

                fig.update_layout(
                    title=f"{var1} vs {var2} (r={correlation:.3f})",
                    xaxis_title=var1,
                    yaxis_title=var2,
                    height=600
                )
                fig = apply_regen_style(fig)
                st.plotly_chart(fig, use_container_width=True)

    # ==================================================================
    # PAGE 6: CUSTOM ANALYSIS
    # ==================================================================
    elif page == "📊 Custom Analysis":
        st.markdown('<h2 class="section-header">📊 Custom Data Analysis</h2>', unsafe_allow_html=True)

        st.markdown("""
        Explore the dataset with custom filters and visualizations.
        """)

        # Variable selection
        numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist()
        valid_cols = [col for col in numeric_cols
                     if data[col].notna().sum() > 100]

        st.subheader("🔍 Variable Distribution Explorer")

        selected_var = st.selectbox("Select Variable to Analyze:", valid_cols)

        if selected_var:
            var_data = pd.to_numeric(data[selected_var], errors='coerce').dropna()

            # Statistics
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.metric("Count", f"{len(var_data):,}")
            with col2:
                st.metric("Mean", f"{var_data.mean():.2f}")
            with col3:
                st.metric("Median", f"{var_data.median():.2f}")
            with col4:
                st.metric("Std Dev", f"{var_data.std():.2f}")
            with col5:
                cv = (var_data.std() / var_data.mean() * 100) if var_data.mean() != 0 else 0
                st.metric("CV", f"{cv:.1f}%")

            # Visualization options
            viz_type = st.radio("Visualization Type:",
                               ["Histogram", "Box Plot", "Violin Plot"])

            if viz_type == "Histogram":
                bins = st.slider("Number of Bins:", 10, 100, 50)
                fig = go.Figure(data=[go.Histogram(x=var_data, nbinsx=bins,
                                                   marker_color='#2c5f2d')])
                fig.add_vline(x=var_data.mean(), line_dash="dash",
                             line_color="red", annotation_text="Mean")
                fig.add_vline(x=var_data.median(), line_dash="dash",
                             line_color="blue", annotation_text="Median")

            elif viz_type == "Box Plot":
                fig = go.Figure(data=[go.Box(y=var_data, marker_color='#2c5f2d')])

            else:  # Violin Plot
                fig = go.Figure(data=[go.Violin(y=var_data, marker_color='#2c5f2d',
                                                box_visible=True, meanline_visible=True)])

            fig.update_layout(
                title=f"Distribution of {selected_var}",
                yaxis_title="Value" if viz_type != "Histogram" else "Frequency",
                xaxis_title=selected_var if viz_type == "Histogram" else "",
                height=500
            )
            fig = apply_regen_style(fig)
            st.plotly_chart(fig, use_container_width=True)

            # Percentiles
            st.subheader("📊 Percentile Distribution")
            percentiles = [0, 10, 25, 50, 75, 90, 100]
            percentile_vals = [var_data.quantile(p/100) for p in percentiles]

            perc_df = pd.DataFrame({
                'Percentile': [f"{p}th" for p in percentiles],
                'Value': [f"{v:.2f}" for v in percentile_vals]
            })

            # Create HTML table with Regen Ag Lab styling
            html_table = '<table class="regen-table" style="width: 100%; border-collapse: collapse; margin: 20px 0; font-family: Raleway, sans-serif;">'
            html_table += '<thead><tr>'
            for col in perc_df.columns:
                html_table += f'<th style="background: linear-gradient(to right, #eb4065, #e40032); color: #ffffff; font-size: 18px; font-weight: 700; padding: 15px; text-align: center; border: 1px solid #e40032;">{col}</th>'
            html_table += '</tr></thead><tbody>'

            for idx, row in perc_df.iterrows():
                bg_color = '#ffffff' if idx % 2 == 0 else '#EEEEEE'
                html_table += '<tr>'
                for val in row:
                    html_table += f'<td style="background: {bg_color}; border: 1px solid #AAAAAA; padding: 10px 15px; text-align: center; font-size: 17px; color: #53575a; line-height: 1.5;">{val}</td>'
                html_table += '</tr>'

            html_table += '</tbody></table>'
            st.markdown(html_table, unsafe_allow_html=True)

    # ==================================================================
    # PAGE 7: DATA DICTIONARY
    # ==================================================================
    elif page == "📚 Data Dictionary":
        st.markdown('<h2 class="section-header">📚 Data Dictionary</h2>', unsafe_allow_html=True)

        st.markdown("""
        Complete reference for all 211 variables in the dataset, organized by category.
        """)

        st.markdown("""
        <div class="info-box">
        <b>Key Haney Test Variables:</b><br>
        • <b>CO2-C</b> - 24-hour CO2 respiration (measures biological activity)<br>
        • <b>H3A extractant results</b> - Mimics weak organic acids from plant roots for accurate nutrient availability<br>
        • <b>WEOC/WEON</b> - Water-extractable organic carbon and nitrogen (food for soil microbes)<br>
        • <b>Soil Health Calculation</b> - Integrated score combining biology + chemistry
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        # Load data dictionary
        dict_file = BASE_DIR / 'DATA_DICTIONARY.md'
        try:
            with open(dict_file, 'r') as f:
                dict_content = f.read()

            # Show summary stats first
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Variables", "211")
            with col2:
                st.metric("Numeric Variables", "94")
            with col3:
                st.metric("Categorical Variables", "117")
            with col4:
                st.metric("Categories", "17")

            st.markdown("---")

            # Add search functionality
            st.subheader("🔍 Search Variables")
            search_term = st.text_input("Enter variable name or keyword:", "")

            if search_term:
                # Filter dictionary content
                lines = dict_content.split('\n')
                filtered_lines = []
                show_context = False
                context_lines = 0

                for line in lines:
                    if search_term.lower() in line.lower():
                        show_context = True
                        context_lines = 10  # Show 10 lines after match

                    if show_context:
                        filtered_lines.append(line)
                        context_lines -= 1
                        if context_lines <= 0:
                            show_context = False
                            filtered_lines.append("\n---\n")

                if filtered_lines:
                    st.markdown('\n'.join(filtered_lines))
                else:
                    st.warning(f"No variables found matching '{search_term}'")
            else:
                # Show full dictionary
                st.markdown(dict_content)

        except FileNotFoundError:
            st.error("Data dictionary file not found. Please ensure DATA_DICTIONARY.md exists in the project directory.")
            st.info(f"Expected location: {dict_file}")

    # ==================================================================
    # PAGE 8: PROJECT DELIVERABLES
    # ==================================================================
    elif page == "📦 Project Deliverables":
        st.markdown('<h2 class="section-header">📦 Project Deliverables & File Inventory</h2>', unsafe_allow_html=True)

        st.markdown("""
        Complete overview of all analysis outputs, reports, and data files.
        """)

        # Summary metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Samples", f"{len(data):,}")
        with col2:
            st.metric("Data Batches", "4")
        with col3:
            st.metric("Visualizations", "15+")
        with col4:
            st.metric("Reports", "Multiple")

        st.markdown("---")

        # Load and display analysis summary
        summary_file = BASE_DIR.parent / 'docs' / 'ANALYSIS_SUMMARY_ALL_BATCHES.md'
        try:
            with open(summary_file, 'r', encoding='utf-8') as f:
                summary_content = f.read()

            st.markdown(summary_content)

        except FileNotFoundError:
            st.warning("Analysis summary not found. Showing basic inventory...")

        # File structure
        st.subheader("📁 Project Structure")

        structure = """
        ```
        agwise_eda/
        ├── 📄 Documentation
        │   ├── README.md
        │   ├── DATA_DICTIONARY.md
        │   ├── ANALYSIS_SUMMARY_ALL_BATCHES.md
        │   └── PROJECT_SUMMARY.md
        │
        ├── 📊 Reports
        │   ├── COMPREHENSIVE_EDA_REPORT_FULL_DATASET.pdf (5.7 MB)
        │   └── EXECUTIVE_SUMMARY_FULL_DATASET.md
        │
        ├── 💾 Data
        │   ├── raw/ (4 batches, 2,504 files)
        │   └── processed/
        │       └── combined_soil_data_FULL.csv (37,310 samples)
        │
        ├── 🐍 Scripts
        │   ├── run_all_analyses.py
        │   ├── 01_eda_analysis.py
        │   ├── 02_eda_visualizations.py
        │   ├── 03_eda_correlations.py
        │   ├── 04_eda_categorical_crops.py
        │   └── 05_eda_advanced_insights.py
        │
        ├── 📈 Outputs
        │   ├── visualizations/ (15+ charts)
        │   └── tables/ (11+ CSV reports)
        │
        └── 🖥️  Dashboard
            └── app.py (this dashboard)
        ```
        """
        st.markdown(structure)

        # Download links section
        st.subheader("📥 Key Downloads")

        st.markdown("""
        **Main Reports:**
        - `reports/COMPREHENSIVE_EDA_REPORT_FULL_DATASET.pdf` - Complete analysis (5.7 MB)
        - `ANALYSIS_SUMMARY_ALL_BATCHES.md` - Executive summary
        - `DATA_DICTIONARY.md` - Variable reference

        **Data Files:**
        - `combined_soil_data.csv` - Full dataset (37,310 samples, 13 MB)
        - `agwise_eda/data/processed/combined_soil_data_FULL.csv` - Dashboard data

        **Analysis Outputs:**
        - `outputs/visualizations/` - All charts (PNG, 300 DPI)
        - `outputs/tables/` - All statistical tables (CSV)
        """)

        # Quality metrics
        st.subheader("✅ Quality Metrics")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            **Data Quality:**
            - ✅ All 4 batches processed
            - ✅ 37,310 total samples
            - ✅ 211 variables tracked
            - ✅ Batch tracking enabled
            - ✅ Missing data documented
            """)

        with col2:
            st.markdown("""
            **Deliverables:**
            - ✅ Comprehensive PDF report
            - ✅ Interactive dashboard (8 views)
            - ✅ 15+ visualizations (300 DPI)
            - ✅ 11+ statistical tables
            - ✅ Complete data dictionary
            """)

    # Footer (added to all pages) - Regen Ag Lab branding
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

else:
    st.error("Unable to load data. Please check that the data file exists.")
    st.info(f"Expected location: {DATA_FILE}")
