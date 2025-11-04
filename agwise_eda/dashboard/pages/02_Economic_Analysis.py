"""
Economic Analysis: Haney vs Traditional Soil Testing
Interactive What-If Simulation Tool powered by Regen Ag Lab data

Robust economic model for agronomic decision-making based on
the Haney Soil Health Test methodology
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from pathlib import Path

st.set_page_config(page_title="Economic Analysis", page_icon="💰", layout="wide", initial_sidebar_state="collapsed")

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

    h1 { font-size: 48px !important; }
    h2 { font-size: 42px !important; }
    h3 { font-size: 30px !important; }
    h4 { font-size: 20px !important; }

    /* Equation box */
    .equation-box {
        background-color: #ffffff;
        padding: 25px 30px;
        border-radius: 5px;
        border-left: 5px solid #e40032;
        margin: 1.5rem 0;
        font-family: 'Courier New', monospace;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }

    /* Assumption header */
    .assumption-header {
        background-color: #ffffff;
        padding: 15px 20px;
        border-radius: 5px;
        font-weight: 600;
        margin-top: 1rem;
        border: 1px solid #eaeaea;
        color: #53575a;
        font-family: 'Raleway', sans-serif;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }

    /* Metrics */
    .metric-positive {
        color: #2e7d32;
        font-weight: 600;
        font-family: 'Raleway', sans-serif;
    }

    .metric-negative {
        color: #c62828;
        font-weight: 600;
        font-family: 'Raleway', sans-serif;
    }

    /* Info boxes */
    .info-box {
        background-color: #ffffff;
        padding: 25px 30px;
        border-radius: 5px;
        border-left: 5px solid #e40032;
        margin: 1.5rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        font-family: 'Raleway', sans-serif;
        color: #53575a;
    }

    /* Streamlit metric styling */
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

    /* Section headers */
    .section-header {
        color: #e40032 !important;
        font-family: 'Raleway', sans-serif !important;
        font-weight: 600 !important;
        border-bottom: 3px solid #e40032;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }

    /* Hide sidebar completely since we're using top navigation */
    [data-testid="stSidebar"] {
        display: none !important;
    }

    button[kind="header"] {
        display: none !important;
    }

    .main {
        margin-left: 0 !important;
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

    /* Expander styling - fix white-on-white issue */
    /* Target multiple versions of Streamlit expander classes */
    .streamlit-expanderHeader,
    [data-testid="stExpander"] summary,
    details summary,
    [data-testid="stExpanderDetails"] summary {
        background-color: #f5f5f5 !important;
        color: #53575a !important;
        font-weight: 600 !important;
        border: 1px solid #eaeaea !important;
        border-radius: 5px !important;
        padding: 15px !important;
        font-family: 'Raleway', sans-serif !important;
        font-size: 17px !important;
    }

    .streamlit-expanderHeader:hover,
    [data-testid="stExpander"] summary:hover,
    details summary:hover,
    [data-testid="stExpanderDetails"] summary:hover {
        background-color: #ffffff !important;
        border-color: #e40032 !important;
    }

    .streamlit-expanderContent,
    [data-testid="stExpander"] [data-testid="stExpanderDetails"],
    details[open] {
        background-color: #ffffff !important;
        border: 1px solid #eaeaea !important;
        border-top: none !important;
        padding: 20px !important;
    }

    /* Ensure expander text is visible */
    [data-testid="stExpander"] p,
    [data-testid="stExpander"] span,
    details summary p,
    details summary span {
        color: #53575a !important;
    }

    /* Expander icon/arrow */
    [data-testid="stExpander"] svg,
    details summary svg {
        color: #53575a !important;
    }
</style>
""", unsafe_allow_html=True)

# Navigation Bar with dropdown - Deployment Ready (Hybrid approach)
st.markdown("""
<style>
    /* Navigation bar container - full width */
    [data-testid="stHorizontalBlock"]:first-of-type {
        background-color: #ffffff;
        border-bottom: 3px solid #e40032;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        padding: 0 max(20px, calc((100vw - 1200px) / 2));
        margin-top: 0;
        margin-bottom: 20px;
        margin-left: calc(-1 * max(0rem, (100% - 1200px) / 2));
        margin-right: calc(-1 * max(0rem, (100% - 1200px) / 2));
        width: 100vw;
        position: relative;
        left: 50%;
        right: 50%;
        transform: translateX(-50%);
    }

    /* Style columns in navbar to be inline */
    [data-testid="stHorizontalBlock"]:first-of-type [data-testid="column"] {
        padding: 0 !important;
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
        padding: 20px 18px !important;
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
nav_cols = st.columns([0.8, 0.5, 0.8, 0.7, 0.6])

with nav_cols[0]:
    st.markdown('<div class="nav-logo">Haney Soil AI</div>', unsafe_allow_html=True)

with nav_cols[1]:
    st.markdown('<a href="/01_Home" target="_self" class="nav-link" style="text-decoration: none;">Home</a>', unsafe_allow_html=True)

with nav_cols[2]:
    # Analysis dropdown (HTML only - uses query params)
    st.markdown("""
    <div style="position: relative; display: inline-block;">
        <div class="nav-item dropdown">
            <span class="nav-link">Analysis <span class="dropdown-arrow">▼</span></span>
            <div class="dropdown-content">
                <a href="/?view=overview" target="_self">📈 Overview & Statistics</a>
                <a href="/?view=soil_health" target="_self">🔬 Soil Health Analysis</a>
                <a href="/?view=cover_crop" target="_self">🌾 Cover Crop Analysis</a>
                <a href="/?view=economic" target="_self">💰 Economic Analysis</a>
                <a href="/?view=correlation" target="_self">🔗 Correlation Explorer</a>
                <a href="/?view=custom" target="_self">📊 Custom Analysis</a>
                <a href="/?view=dictionary" target="_self">📚 Data Dictionary</a>
                <a href="/?view=deliverables" target="_self">📦 Project Deliverables</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with nav_cols[3]:
    st.markdown('<a href="/02_Economic_Analysis" target="_self" class="nav-link" style="text-decoration: none;">Economic Analysis</a>', unsafe_allow_html=True)

with nav_cols[4]:
    st.markdown('<a href="/03_Feedback" target="_self" class="nav-link" style="text-decoration: none;">Feedback</a>', unsafe_allow_html=True)

# Apply Regen Ag Lab styling to Plotly figures
def apply_regen_style(fig):
    """Apply consistent Regen Ag Lab brand styling to Plotly figures"""
    fig.update_layout(
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
            color='#53575a',
            weight=600
        ),
        hoverlabel=dict(
            bgcolor='#ffffff',
            font_size=14,
            font_family='Raleway, sans-serif'
        )
    )

    # Update axes styling
    fig.update_xaxes(
        gridcolor='#dddddd',
        tickfont=dict(color='#53575a', family='Raleway, sans-serif')
    )
    fig.update_yaxes(
        gridcolor='#dddddd',
        tickfont=dict(color='#53575a', family='Raleway, sans-serif')
    )

    return fig


st.markdown('<h2 class="section-header">💰 Economic Analysis: Soil Testing ROI</h2>', unsafe_allow_html=True)
st.markdown("### Interactive What-If Simulation for Haney vs Traditional Testing")

st.markdown("""
<div class="info-box">
<b>About the Haney Test Economic Advantage:</b> The Haney Soil Health Test methodology provides more accurate
plant-available nutrient measurements by measuring soil as a living system. This analysis demonstrates the economic
value of reduced synthetic fertilizer inputs based on biological nutrient availability data.
<br><br>
<b>Data powered by Regen Ag Lab</b> - Developed by Dr. Rick Haney, Chief Scientific Officer
</div>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    data_file = Path(__file__).parent.parent.parent / 'data' / 'processed' / 'combined_soil_data_FULL.csv'
    df = pd.read_csv(data_file)
    return df

try:
    df = load_data()
    st.markdown(f'''
    <div style="background-color: #f5f5f5; border-left: 4px solid #e40032; padding: 15px; margin: 15px 0; font-family: Raleway, sans-serif;">
        <p style="color: #53575a; margin: 0; font-size: 17px;">✓ Loaded {len(df):,} soil samples for analysis</p>
    </div>
    ''', unsafe_allow_html=True)
except:
    st.markdown('''
    <div style="background-color: #f5f5f5; border-left: 4px solid #e40032; padding: 15px; margin: 15px 0; font-family: Raleway, sans-serif;">
        <p style="color: #e40032; margin: 0; font-size: 17px; font-weight: 600;">⚠ Could not load data. Using synthetic data for demonstration.</p>
    </div>
    ''', unsafe_allow_html=True)
    df = pd.DataFrame({
        'Traditional N Rec': np.random.normal(27, 15, 1000),
        'Available N (Haney)': np.random.normal(60, 35, 1000)
    })

# ============================================================================
# SECTION 1: ASSUMPTIONS & PARAMETERS
# ============================================================================

st.markdown("---")
st.markdown("## 📋 Model Assumptions & Parameters")

col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='assumption-header'>🧪 Testing Parameters</div>", unsafe_allow_html=True)

    haney_cost = st.slider(
        "Haney Test Cost ($/sample)",
        min_value=30.0, max_value=100.0, value=50.0, step=5.0,
        help="Typical range: $45-65 per sample"
    )

    traditional_cost = st.slider(
        "Traditional Test Cost ($/sample)",
        min_value=10.0, max_value=50.0, value=25.0, step=2.5,
        help="Typical range: $20-35 per sample"
    )

    num_depths = st.slider(
        "Sampling Depths per Location",
        min_value=1, max_value=4, value=1, step=1,
        help="Common: 1 (0-6\") or 2 (0-6\", 6-12\")"
    )

    acres_per_field = st.slider(
        "Average Field Size (acres)",
        min_value=10, max_value=500, value=80, step=10,
        help="Used to calculate per-acre economics"
    )

    samples_per_field = st.slider(
        "Samples per Field",
        min_value=1, max_value=20, value=4, step=1,
        help="More samples = better spatial resolution"
    )

    testing_frequency_years = st.slider(
        "Testing Frequency (years)",
        min_value=1, max_value=5, value=3, step=1,
        help="How often do you test? (every X years)"
    )

with col2:
    st.markdown("<div class='assumption-header'>🌾 Crop & Economic Parameters</div>", unsafe_allow_html=True)

    nitrogen_price = st.slider(
        "Nitrogen Price ($/lb N)",
        min_value=0.40, max_value=1.50, value=0.75, step=0.05,
        help="Anhydrous ammonia ~$0.50-0.70, Urea ~$0.60-0.90, UAN ~$0.70-1.00"
    )

    application_cost = st.slider(
        "Application Cost ($/acre)",
        min_value=5.0, max_value=25.0, value=12.0, step=1.0,
        help="Custom application or equipment cost per acre"
    )

    crop_type = st.selectbox(
        "Primary Crop",
        ["Corn", "Soybeans", "Wheat", "Cotton", "Other"],
        help="Different crops have different N response curves"
    )

    # Crop-specific parameters
    if crop_type == "Corn":
        n_response_efficiency = st.slider(
            "N Use Efficiency (%)",
            min_value=30, max_value=70, value=50, step=5,
            help="% of applied N actually used by crop"
        )
        yield_response_per_lb_n = st.slider(
            "Yield Response (bu/acre per lb N)",
            min_value=0.5, max_value=2.0, value=1.0, step=0.1,
            help="Additional yield per lb N applied (diminishing returns assumed)"
        )
        corn_price = st.slider(
            "Corn Price ($/bu)",
            min_value=3.0, max_value=8.0, value=5.50, step=0.25
        )
    else:
        n_response_efficiency = 50
        yield_response_per_lb_n = 0.5
        corn_price = 5.50

    environmental_cost = st.slider(
        "Environmental/Risk Cost ($/lb excess N)",
        min_value=0.0, max_value=0.50, value=0.10, step=0.05,
        help="Cost of N leaching, runoff, regulatory risk (often overlooked)"
    )

# ============================================================================
# SECTION 2: MATHEMATICAL MODEL
# ============================================================================

st.markdown("---")
st.markdown("## 🧮 Economic Model Equations")

with st.expander("📐 View Detailed Equations", expanded=False):
    st.markdown("""
    ### Core Economic Model

    #### 1. Testing Costs
    ```
    Total_Test_Cost = (Test_Cost_per_Sample × Samples_per_Field × Depths × Fields) / Testing_Frequency

    Annual_Test_Cost_per_Acre = Total_Test_Cost / (Fields × Acres_per_Field × Testing_Frequency)
    ```

    #### 2. Nitrogen Recommendation Difference
    ```
    ΔN = N_Traditional - N_Haney

    where:
        N_Traditional = Traditional soil test N recommendation (lbs/acre)
        N_Haney = Haney test available N (lbs/acre)
        ΔN = Difference in N recommendation (typically positive)
    ```

    #### 3. Fertilizer Cost Impact
    ```
    Fertilizer_Cost_Savings = ΔN × N_Price × Acres

    Application_Cost_Savings = (ΔN / Typical_Application_Rate) × Application_Cost × Acres
        where Typical_Application_Rate = 100 lbs N/acre
    ```

    #### 4. Yield Impact (Precision N Management)
    ```
    Yield_Value_Change = (ΔN × N_Use_Efficiency/100 × Yield_Response × Crop_Price) × Acres

    Note: Assumes Haney test provides more accurate N recommendation,
          reducing both over-application and under-application risk
    ```

    #### 5. Environmental Cost Savings
    ```
    Environmental_Savings = |ΔN| × Environmental_Cost × Acres

    (Avoided costs: nitrate leaching, water quality, regulatory compliance)
    ```

    #### 6. Net Economic Benefit
    ```
    Annual_Net_Benefit = (Fertilizer_Savings + Application_Savings + Yield_Value + Environmental_Savings)
                        - (Haney_Test_Cost - Traditional_Test_Cost)

    Payback_Period = (Haney_Test_Cost - Traditional_Test_Cost) / Annual_Net_Benefit

    ROI = (Annual_Net_Benefit × Years) / Additional_Test_Investment × 100%
    ```

    #### 7. Break-Even Analysis
    ```
    Break_Even_Acres = (Haney_Cost - Traditional_Cost) × Samples / (ΔN × N_Price)
    ```
    """)

# ============================================================================
# SECTION 3: CALCULATIONS FROM ACTUAL DATA
# ============================================================================

st.markdown("---")
st.markdown("## 📊 Analysis Based on Your Data")

# Get actual nitrogen data
trad_col = None
haney_col = None

for col in df.columns:
    if 'traditional' in col.lower() and 'rec' in col.lower():
        trad_col = col
    if 'available n' in col.lower() or ('haney' in col.lower() and 'n' in col.lower()):
        haney_col = col

if trad_col and haney_col:
    # Filter valid data
    valid_data = df[[trad_col, haney_col]].dropna()

    if len(valid_data) > 0:
        traditional_n_mean = valid_data[trad_col].mean()
        haney_n_mean = valid_data[haney_col].mean()
        n_difference_mean = haney_n_mean - traditional_n_mean
        n_difference_median = valid_data[haney_col].median() - valid_data[trad_col].median()

        st.success(f"✓ Using actual data: {len(valid_data):,} samples with both Traditional and Haney N values")
    else:
        st.warning("Using estimated values based on literature")
        traditional_n_mean = 27.0
        haney_n_mean = 60.0
        n_difference_mean = 33.0
        n_difference_median = 31.0
else:
    traditional_n_mean = 27.0
    haney_n_mean = 60.0
    n_difference_mean = 33.0
    n_difference_median = 31.0

# ============================================================================
# SECTION 4: ECONOMIC CALCULATIONS
# ============================================================================

# Total samples needed
total_samples_per_field = samples_per_field * num_depths
annual_test_cost_traditional = (traditional_cost * total_samples_per_field) / testing_frequency_years
annual_test_cost_haney = (haney_cost * total_samples_per_field) / testing_frequency_years
additional_test_cost = annual_test_cost_haney - annual_test_cost_traditional

# Per acre testing cost
test_cost_per_acre_traditional = annual_test_cost_traditional / acres_per_field
test_cost_per_acre_haney = annual_test_cost_haney / acres_per_field

# Nitrogen savings
fertilizer_savings_per_acre = n_difference_mean * nitrogen_price
application_savings_per_acre = (n_difference_mean / 100) * application_cost if n_difference_mean > 10 else 0

# Yield impact (assuming better precision with Haney)
# Conservative: assume 20% of excess N was actually needed, 80% was waste
precision_value_per_acre = (n_difference_mean * 0.2 * (n_response_efficiency/100) *
                            yield_response_per_lb_n * corn_price)

# Environmental savings
environmental_savings_per_acre = abs(n_difference_mean) * environmental_cost

# Total savings
total_savings_per_acre = (fertilizer_savings_per_acre +
                         application_savings_per_acre +
                         precision_value_per_acre +
                         environmental_savings_per_acre)

net_benefit_per_acre = total_savings_per_acre - (test_cost_per_acre_haney - test_cost_per_acre_traditional)

# Field level
net_benefit_per_field = net_benefit_per_acre * acres_per_field
total_field_savings = net_benefit_per_field * testing_frequency_years

# Break-even
if fertilizer_savings_per_acre > 0:
    breakeven_acres = additional_test_cost / fertilizer_savings_per_acre
else:
    breakeven_acres = float('inf')

# ROI
if additional_test_cost > 0:
    roi_1_year = (net_benefit_per_acre * acres_per_field) / additional_test_cost * 100
    roi_3_year = (net_benefit_per_acre * acres_per_field * 3) / (additional_test_cost * 3) * 100
else:
    roi_1_year = 0
    roi_3_year = 0

# ============================================================================
# SECTION 5: RESULTS DASHBOARD
# ============================================================================

st.markdown("---")
st.markdown("## 💡 Economic Results")

# Key metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Net Benefit per Acre",
        f"${net_benefit_per_acre:.2f}",
        delta=f"{roi_1_year:.1f}% ROI" if net_benefit_per_acre > 0 else None,
        delta_color="normal" if net_benefit_per_acre > 0 else "inverse"
    )

with col2:
    st.metric(
        "Total Field Benefit",
        f"${net_benefit_per_field:,.2f}",
        delta=f"{acres_per_field} acres"
    )

with col3:
    st.metric(
        "Break-Even Field Size",
        f"{breakeven_acres:.1f} acres" if breakeven_acres != float('inf') else "N/A",
        delta="per test cycle"
    )

with col4:
    st.metric(
        "N Savings per Acre",
        f"{n_difference_mean:.1f} lbs N",
        delta=f"${fertilizer_savings_per_acre:.2f}"
    )

# Detailed breakdown
st.markdown("### 📈 Detailed Cost-Benefit Breakdown (Per Acre, Annualized)")

breakdown_data = {
    'Category': [
        'Testing Cost (Traditional)',
        'Testing Cost (Haney)',
        'Additional Testing Investment',
        '',
        'Fertilizer Cost Savings',
        'Application Cost Savings',
        'Precision Value Gain',
        'Environmental Savings',
        '',
        'Total Savings',
        'Net Benefit'
    ],
    'Amount ($/acre)': [
        -test_cost_per_acre_traditional,
        -test_cost_per_acre_haney,
        -(test_cost_per_acre_haney - test_cost_per_acre_traditional),
        0,
        fertilizer_savings_per_acre,
        application_savings_per_acre,
        precision_value_per_acre,
        environmental_savings_per_acre,
        0,
        total_savings_per_acre,
        net_benefit_per_acre
    ],
    'Description': [
        f"${traditional_cost}/sample × {total_samples_per_field} samples ÷ {testing_frequency_years} yrs ÷ {acres_per_field} ac",
        f"${haney_cost}/sample × {total_samples_per_field} samples ÷ {testing_frequency_years} yrs ÷ {acres_per_field} ac",
        "Additional investment for Haney testing",
        "",
        f"{n_difference_mean:.1f} lbs N × ${nitrogen_price:.2f}/lb",
        f"Reduced application trips/equipment use",
        f"Improved N management precision, reduced risk",
        f"{abs(n_difference_mean):.1f} lbs excess N × ${environmental_cost:.2f}/lb",
        "",
        "Sum of all savings categories",
        "Total Savings - Additional Test Investment"
    ]
}

breakdown_df = pd.DataFrame(breakdown_data)

# Color coding
def color_amount(val):
    if val > 0:
        return f'<span class="metric-positive">+${val:.2f}</span>'
    elif val < 0:
        return f'<span class="metric-negative">-${abs(val):.2f}</span>'
    else:
        return ''

breakdown_df['Amount Display'] = breakdown_df['Amount ($/acre)'].apply(color_amount)

st.markdown(breakdown_df[['Category', 'Amount Display', 'Description']].to_html(escape=False, index=False),
            unsafe_allow_html=True)

# ============================================================================
# SECTION 6: VISUALIZATIONS
# ============================================================================

st.markdown("---")
st.markdown("## 📊 Interactive Visualizations")

# Visualization 1: Waterfall chart
fig_waterfall = go.Figure(go.Waterfall(
    name = "Economic Analysis",
    orientation = "v",
    measure = ["relative", "relative", "relative", "relative", "relative", "total"],
    x = ["Additional<br>Test Cost", "Fertilizer<br>Savings", "Application<br>Savings",
         "Precision<br>Value", "Environmental<br>Savings", "Net<br>Benefit"],
    textposition = "outside",
    text = [f"-${additional_test_cost/acres_per_field:.2f}",
            f"+${fertilizer_savings_per_acre:.2f}",
            f"+${application_savings_per_acre:.2f}",
            f"+${precision_value_per_acre:.2f}",
            f"+${environmental_savings_per_acre:.2f}",
            f"${net_benefit_per_acre:.2f}"],
    y = [-additional_test_cost/acres_per_field,
         fertilizer_savings_per_acre,
         application_savings_per_acre,
         precision_value_per_acre,
         environmental_savings_per_acre,
         net_benefit_per_acre],
    connector = {"line":{"color":"rgb(63, 63, 63)"}},
    decreasing = {"marker":{"color":"#c62828"}},
    increasing = {"marker":{"color":"#2e7d32"}},
    totals = {"marker":{"color":"#1565c0"}}
))

fig_waterfall.update_layout(
    title = "Economic Waterfall: Haney Testing ROI ($/acre)",
    showlegend = False,
    height = 500
)

fig_waterfall = apply_regen_style(fig_waterfall)
st.plotly_chart(fig_waterfall, use_container_width=True)

# Visualization 2: Sensitivity Analysis
st.markdown("### 🎯 Sensitivity Analysis: How Do Key Variables Affect ROI?")

sensitivity_var = st.selectbox(
    "Select Variable to Analyze",
    ["Nitrogen Price", "Field Size", "N Difference", "Haney Test Cost", "Testing Frequency"]
)

if sensitivity_var == "Nitrogen Price":
    x_range = np.linspace(0.40, 1.50, 50)
    y_values = [(n_difference_mean * x - (test_cost_per_acre_haney - test_cost_per_acre_traditional))
                for x in x_range]
    x_label = "Nitrogen Price ($/lb)"
    current_val = nitrogen_price

elif sensitivity_var == "Field Size":
    x_range = np.linspace(10, 500, 50)
    y_values = []
    for acres in x_range:
        test_cost_diff = ((haney_cost - traditional_cost) * total_samples_per_field / testing_frequency_years) / acres
        savings = fertilizer_savings_per_acre + application_savings_per_acre + precision_value_per_acre + environmental_savings_per_acre
        y_values.append(savings - test_cost_diff)
    x_label = "Field Size (acres)"
    current_val = acres_per_field

elif sensitivity_var == "N Difference":
    x_range = np.linspace(0, 80, 50)
    y_values = []
    for delta_n in x_range:
        fert_save = delta_n * nitrogen_price
        app_save = (delta_n / 100) * application_cost if delta_n > 10 else 0
        prec_val = (delta_n * 0.2 * (n_response_efficiency/100) * yield_response_per_lb_n * corn_price)
        env_save = delta_n * environmental_cost
        y_values.append(fert_save + app_save + prec_val + env_save - (test_cost_per_acre_haney - test_cost_per_acre_traditional))
    x_label = "N Difference: Haney - Traditional (lbs/acre)"
    current_val = n_difference_mean

elif sensitivity_var == "Haney Test Cost":
    x_range = np.linspace(30, 100, 50)
    y_values = []
    for cost in x_range:
        test_cost_diff = ((cost - traditional_cost) * total_samples_per_field / testing_frequency_years) / acres_per_field
        savings = fertilizer_savings_per_acre + application_savings_per_acre + precision_value_per_acre + environmental_savings_per_acre
        y_values.append(savings - test_cost_diff)
    x_label = "Haney Test Cost ($/sample)"
    current_val = haney_cost

else:  # Testing Frequency
    x_range = np.linspace(1, 5, 5)
    y_values = []
    for freq in x_range:
        test_cost_diff = ((haney_cost - traditional_cost) * total_samples_per_field / freq) / acres_per_field
        savings = fertilizer_savings_per_acre + application_savings_per_acre + precision_value_per_acre + environmental_savings_per_acre
        y_values.append(savings - test_cost_diff)
    x_label = "Testing Frequency (years)"
    current_val = testing_frequency_years

fig_sensitivity = go.Figure()

fig_sensitivity.add_trace(go.Scatter(
    x=x_range,
    y=y_values,
    mode='lines',
    name='Net Benefit',
    line=dict(color='#2e7d32', width=3)
))

# Add zero line
fig_sensitivity.add_hline(y=0, line_dash="dash", line_color="red",
                          annotation_text="Break-Even", annotation_position="right")

# Add current value marker
fig_sensitivity.add_vline(x=current_val, line_dash="dot", line_color="blue",
                         annotation_text="Current", annotation_position="top")

fig_sensitivity.update_layout(
    title=f"Sensitivity: Net Benefit per Acre vs {sensitivity_var}",
    xaxis_title=x_label,
    yaxis_title="Net Benefit ($/acre)",
    height=500,
    hovermode='x unified'
)

fig_sensitivity = apply_regen_style(fig_sensitivity)
st.plotly_chart(fig_sensitivity, use_container_width=True)

# Visualization 3: Multi-variable scenario matrix
st.markdown("### 🎲 Scenario Matrix: Field Size × Nitrogen Price")

field_sizes = np.array([20, 40, 80, 160, 320])
n_prices = np.array([0.50, 0.65, 0.75, 0.90, 1.20])

scenario_matrix = np.zeros((len(n_prices), len(field_sizes)))

for i, n_price in enumerate(n_prices):
    for j, field_size in enumerate(field_sizes):
        test_cost_diff = ((haney_cost - traditional_cost) * total_samples_per_field / testing_frequency_years) / field_size
        fert_save = n_difference_mean * n_price
        app_save = (n_difference_mean / 100) * application_cost if n_difference_mean > 10 else 0
        prec_val = (n_difference_mean * 0.2 * (n_response_efficiency/100) * yield_response_per_lb_n * corn_price)
        env_save = n_difference_mean * environmental_cost
        scenario_matrix[i, j] = fert_save + app_save + prec_val + env_save - test_cost_diff

fig_heatmap = go.Figure(data=go.Heatmap(
    z=scenario_matrix,
    x=field_sizes,
    y=n_prices,
    colorscale='RdYlGn',
    text=np.round(scenario_matrix, 2),
    texttemplate='$%{text}',
    textfont={"size":12},
    colorbar=dict(title="Net Benefit<br>($/acre)")
))

fig_heatmap.update_layout(
    title="Scenario Analysis: Net Benefit per Acre",
    xaxis_title="Field Size (acres)",
    yaxis_title="Nitrogen Price ($/lb)",
    height=500
)

fig_heatmap = apply_regen_style(fig_heatmap)
st.plotly_chart(fig_heatmap, use_container_width=True)

# ============================================================================
# SECTION 7: RECOMMENDATIONS
# ============================================================================

st.markdown("---")
st.markdown("## 🎯 Recommendations & Decision Framework")

if net_benefit_per_acre > 5:
    st.markdown(f"""<div style="background-color: #f5f5f5; border-left: 4px solid #e40032; padding: 20px; margin: 20px 0; font-family: Raleway, sans-serif; border-radius: 5px;">
<h3 style="color: #e40032; margin-top: 0; font-size: 24px; font-weight: 600;">✅ Strong Economic Case for Haney Testing</h3>
<p style="color: #53575a; font-size: 17px; margin: 15px 0; line-height: 1.7;">
<strong>Net benefit of ${net_benefit_per_acre:.2f}/acre justifies the additional testing investment.</strong>
</p>
<p style="color: #53575a; font-size: 17px; margin: 10px 0; font-weight: 600;">Key Drivers:</p>
<ul style="color: #53575a; font-size: 17px; line-height: 1.7; margin: 10px 0;">
<li>Nitrogen savings: ${fertilizer_savings_per_acre:.2f}/acre</li>
<li>Break-even at {breakeven_acres:.1f} acres (you have {acres_per_field} acres)</li>
<li>ROI: {roi_1_year:.1f}% in first year</li>
</ul>
<p style="color: #53575a; font-size: 17px; margin: 15px 0; line-height: 1.7;">
<strong>Recommended Action:</strong> Adopt Haney testing for improved N management precision.
</p>
</div>""", unsafe_allow_html=True)
elif net_benefit_per_acre > 0:
    st.markdown(f"""<div style="background-color: #f5f5f5; border-left: 4px solid #53575a; padding: 20px; margin: 20px 0; font-family: Raleway, sans-serif; border-radius: 5px;">
<h3 style="color: #53575a; margin-top: 0; font-size: 24px; font-weight: 600;">⚖️ Marginal Economic Case</h3>
<p style="color: #53575a; font-size: 17px; margin: 15px 0; line-height: 1.7;">
<strong>Net benefit of ${net_benefit_per_acre:.2f}/acre is positive but modest.</strong>
</p>
<p style="color: #53575a; font-size: 17px; margin: 10px 0; font-weight: 600;">Considerations:</p>
<ul style="color: #53575a; font-size: 17px; line-height: 1.7; margin: 10px 0;">
<li>May become more attractive with larger field sizes or higher N prices</li>
<li>Environmental benefits provide additional non-quantified value</li>
<li>Consider for high-value fields or problematic soils first</li>
</ul>
<p style="color: #53575a; font-size: 17px; margin: 15px 0; line-height: 1.7;">
<strong>Recommended Action:</strong> Pilot on select fields, evaluate results.
</p>
</div>""", unsafe_allow_html=True)
else:
    st.markdown(f"""<div style="background-color: #f5f5f5; border-left: 4px solid #e40032; padding: 20px; margin: 20px 0; font-family: Raleway, sans-serif; border-radius: 5px;">
<h3 style="color: #e40032; margin-top: 0; font-size: 24px; font-weight: 600;">⚠️ Economics Currently Unfavorable</h3>
<p style="color: #53575a; font-size: 17px; margin: 15px 0; line-height: 1.7;">
<strong>Net benefit of ${net_benefit_per_acre:.2f}/acre suggests traditional testing is more economical under current assumptions.</strong>
</p>
<p style="color: #53575a; font-size: 17px; margin: 10px 0; font-weight: 600;">Factors that could change the analysis:</p>
<ul style="color: #53575a; font-size: 17px; line-height: 1.7; margin: 10px 0;">
<li>Larger field sizes (break-even: {breakeven_acres:.1f} acres)</li>
<li>Higher nitrogen prices</li>
<li>More samples per field (reducing per-acre test cost)</li>
<li>Different crop with higher N response</li>
</ul>
<p style="color: #53575a; font-size: 17px; margin: 15px 0; line-height: 1.7;">
<strong>Recommended Action:</strong> Re-evaluate if conditions change.
</p>
</div>""", unsafe_allow_html=True)

# Additional insights
with st.expander("📚 Additional Considerations"):
    st.markdown("""
    ### Non-Quantified Benefits of Haney Testing:

    1. **Risk Management**
       - Reduced over-fertilization risk
       - Better compliance with nutrient management regulations
       - Improved documentation for sustainability certifications

    2. **Soil Health Insights**
       - Haney test provides soil respiration data (biological activity)
       - Better understanding of organic matter quality
       - Water-extractable organic carbon (WEOC) measurements

    3. **Long-Term Soil Building**
       - More accurate picture supports soil health investments
       - Can track biological improvements over time
       - Aligns with regenerative agriculture goals

    4. **Precision Agriculture Integration**
       - Better data for variable rate N applications
       - Improves predictive models
       - Supports zone management decisions

    ### Limitations of This Analysis:

    - Assumes uniform soil conditions across field
    - Does not account for spatial variability benefits
    - Yield response curves are simplified (reality: diminishing returns)
    - Weather and management factors not included
    - Environmental costs are estimates (regulatory landscape varies)

    ### Next Steps for Validation:

    1. Conduct on-farm trials with split fields (Haney vs Traditional)
    2. Track actual N applications and yields
    3. Measure soil health improvements over multiple years
    4. Calculate actual ROI with your specific data
    """)

# ============================================================================
# SECTION 8: EXPORT RESULTS
# ============================================================================

st.markdown("---")
st.markdown("## 📥 Export Analysis")

if st.button("Generate PDF Report"):
    st.info("PDF generation feature coming soon. Currently, use browser print to save as PDF.")

# CSV export of scenarios
export_scenarios = []
for field_size in [20, 40, 80, 160, 320]:
    for n_price in [0.50, 0.65, 0.75, 0.90, 1.20]:
        test_cost_diff = ((haney_cost - traditional_cost) * total_samples_per_field / testing_frequency_years) / field_size
        fert_save = n_difference_mean * n_price
        app_save = (n_difference_mean / 100) * application_cost if n_difference_mean > 10 else 0
        prec_val = (n_difference_mean * 0.2 * (n_response_efficiency/100) * yield_response_per_lb_n * corn_price)
        env_save = n_difference_mean * environmental_cost
        net = fert_save + app_save + prec_val + env_save - test_cost_diff

        export_scenarios.append({
            'Field_Size_Acres': field_size,
            'N_Price_per_lb': n_price,
            'Test_Cost_Difference_per_Acre': test_cost_diff,
            'Fertilizer_Savings_per_Acre': fert_save,
            'Application_Savings_per_Acre': app_save,
            'Precision_Value_per_Acre': prec_val,
            'Environmental_Savings_per_Acre': env_save,
            'Net_Benefit_per_Acre': net,
            'Total_Field_Benefit': net * field_size
        })

export_df = pd.DataFrame(export_scenarios)

csv = export_df.to_csv(index=False)
st.download_button(
    label="📊 Download Scenario Analysis (CSV)",
    data=csv,
    file_name="haney_economic_scenarios.csv",
    mime="text/csv"
)

# Footer with Regen Ag Lab branding
st.markdown("<hr style='border: none; height: 1px; background-color: #dddddd; margin: 30px 0;'>", unsafe_allow_html=True)

# Convert logo to base64 for embedding
import base64
from pathlib import Path

LOGO_PATH = Path(__file__).parent.parent / 'assets' / 'regen_ag_lab_logo.png'

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
            <p style="margin: 20px 0 0 0; font-size: 14px; color: #888; font-family: 'Raleway', sans-serif;">
                <em>Economic Analysis Tool v1.0 | Model assumptions based on agronomic research and industry standards.<br>
                For specific recommendations, consult with a certified crop advisor or agronomist.</em>
            </p>
        </div>
        <div style="text-align: right;">
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
