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

    header[data-testid="stHeader"] {
        display: none !important;
    }

    .stApp > header {
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

# Navigation Bar
st.markdown("""
<div class="top-nav">
    <div class="nav-container">
        <div class="nav-logo">Haney Soil AI</div>
        <ul class="nav-menu">
            <li class="nav-item"><a href="../" target="_parent" class="nav-link">Home</a></li>
            <li class="nav-item dropdown">
                <span class="nav-link">Analysis <span class="dropdown-arrow">▼</span></span>
                <div class="dropdown-content">
                    <a href="../" target="_parent">📈 Overview & Statistics</a>
                    <a href="../?view=soil_health" target="_parent">🔬 Soil Health Analysis</a>
                    <a href="../?view=cover_crop" target="_parent">🌾 Cover Crop Analysis</a>
                    <a href="../?view=economic" target="_parent">💰 Economic Analysis</a>
                    <a href="../?view=correlation" target="_parent">🔗 Correlation Explorer</a>
                    <a href="../?view=custom" target="_parent">📊 Custom Analysis</a>
                    <a href="../?view=dictionary" target="_parent">📚 Data Dictionary</a>
                    <a href="../?view=deliverables" target="_parent">📦 Project Deliverables</a>
                </div>
            </li>
            <li class="nav-item"><a href="Economic_Analysis" target="_parent" class="nav-link">Economic Analysis</a></li>
            <li class="nav-item"><a href="Feedback" target="_parent" class="nav-link active">Feedback</a></li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)


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
