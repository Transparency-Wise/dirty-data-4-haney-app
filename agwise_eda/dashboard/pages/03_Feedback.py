"""
Feedback Page - Haney Soil AI Dashboard
User feedback submission interface
"""

import streamlit as st
import pandas as pd
import datetime
from pathlib import Path

st.set_page_config(page_title="Feedback", page_icon="💬", layout="wide", initial_sidebar_state="collapsed")

# Setup paths
BASE_DIR = Path(__file__).resolve().parent.parent
FEEDBACK_DIR = BASE_DIR / 'feedback'
FEEDBACK_FILE = FEEDBACK_DIR / 'user_feedback.csv'
FEEDBACK_UPLOADS = FEEDBACK_DIR / 'uploads'

# Ensure feedback directories exist
FEEDBACK_DIR.mkdir(parents=True, exist_ok=True)
FEEDBACK_UPLOADS.mkdir(parents=True, exist_ok=True)

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

    /* Section headers */
    .section-header {
        color: #e40032 !important;
        font-family: 'Raleway', sans-serif !important;
        font-weight: 600 !important;
        border-bottom: 3px solid #e40032;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }

    /* Hide sidebar */
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
        font-weight: 700;
        color: #e40032;
        padding: 15px 20px 15px 0;
    }

    .nav-menu {
        list-style: none;
        margin: 0;
        padding: 0;
        display: flex;
        flex: 1;
    }

    .nav-item {
        position: relative;
    }

    .nav-link {
        display: block;
        padding: 20px 18px;
        color: #53575a !important;
        text-decoration: none !important;
        font-weight: 500;
        transition: color 0.2s ease;
        font-size: 16px;
    }

    .nav-link:hover {
        color: #e40032 !important;
        background-color: #f5f5f5;
        text-decoration: none !important;
    }

    .nav-link.active {
        color: #e40032 !important;
        border-bottom: 3px solid #e40032;
        margin-bottom: -3px;
        text-decoration: none !important;
    }

    /* Dropdown styling */
    .dropdown {
        position: relative;
    }

    .dropdown-content {
        display: none;
        position: absolute;
        background-color: #ffffff;
        min-width: 250px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        z-index: 1000;
        border-top: 3px solid #e40032;
        border-radius: 0 0 5px 5px;
    }

    .dropdown-content a {
        color: #53575a !important;
        padding: 12px 16px;
        text-decoration: none !important;
        display: block;
        font-size: 15px;
        transition: background-color 0.2s ease;
    }

    .dropdown-content a:hover {
        background-color: #f5f5f5;
        color: #e40032 !important;
        padding-left: 25px;
        text-decoration: none !important;
    }

    .dropdown:hover .dropdown-content {
        display: block;
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
        padding: 0 20px;
        margin-top: 0;
        margin-bottom: 20px;
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


# Feedback system function
def save_feedback(page, feedback_type, message, uploaded_file=None):
    """Save user feedback to CSV file"""
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

# Main feedback form
st.markdown('<h2 class="section-header">💬 Submit Feedback</h2>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    feedback_type = st.selectbox(
        "Feedback Type:",
        ["Question", "Comment", "Bug Report", "Feature Request", "Data Issue", "Other"],
        key="feedback_type"
    )

    feedback_message = st.text_area(
        "Your Message:",
        placeholder="Describe your feedback here...",
        height=200,
        key="feedback_message"
    )

    uploaded_file = st.file_uploader(
        "Attach a file (optional):",
        type=['png', 'jpg', 'jpeg', 'pdf', 'csv', 'xlsx', 'txt', 'docx'],
        key="feedback_file"
    )

    if st.button("📤 Submit Feedback", key="submit_feedback", type="primary"):
        if feedback_message.strip():
            try:
                save_feedback(
                    page="Feedback Page",
                    feedback_type=feedback_type,
                    message=feedback_message,
                    uploaded_file=uploaded_file
                )
                st.success("✅ Feedback submitted successfully! Thank you!")
                st.balloons()
            except Exception as e:
                st.error(f"❌ Error submitting feedback: {e}")
        else:
            st.warning("⚠️ Please enter a message before submitting.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #53575a; font-size: 15px; padding: 20px 0;">
    <p>Haney Soil AI Dashboard | Powered by Regen Ag Lab</p>
</div>
""", unsafe_allow_html=True)
