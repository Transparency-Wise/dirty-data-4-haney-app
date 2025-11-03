"""
Regen Ag Lab Style Example Page
Demonstrates proper implementation of Regen Ag Lab brand styling

This page serves as a reference for implementing the brand style guide across the dashboard.
Based on: https://regenaglab.com/
"""

import streamlit as st
from pathlib import Path
from PIL import Image
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Regen Ag Lab - Style Example",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS following Regen Ag Lab Style Guide
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
        --color-medium-gray: #3a3a3a;
        --color-border-light: #dddddd;
        --color-border-medium: #eaeaea;
        --color-table-gray: #EEEEEE;
        --color-table-border: #AAAAAA;
        --color-red-gradient-light: #eb4065;

        --font-family: 'Raleway', sans-serif;
        --font-size-base: 17px;
        --font-weight-normal: 400;
        --font-weight-semibold: 600;
        --font-weight-bold: 700;

        --border-radius: 5px;
        --spacing-unit: 15px;
    }

    /* Override Streamlit defaults - background and fonts */
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

    /* Headings following brand typography */
    h1, .regen-h1 {
        font-family: 'Raleway', sans-serif !important;
        font-size: 48px !important;
        font-weight: 600 !important;
        line-height: 1.7 !important;
        color: #53575a !important;
        margin-bottom: 1rem !important;
    }

    h2, .regen-h2 {
        font-family: 'Raleway', sans-serif !important;
        font-size: 42px !important;
        font-weight: 600 !important;
        line-height: 1.7 !important;
        color: #53575a !important;
        margin-bottom: 1rem !important;
    }

    h3, .regen-h3 {
        font-family: 'Raleway', sans-serif !important;
        font-size: 30px !important;
        font-weight: 600 !important;
        line-height: 1.7 !important;
        color: #53575a !important;
        margin-bottom: 0.8rem !important;
    }

    h4, .regen-h4 {
        font-family: 'Raleway', sans-serif !important;
        font-size: 20px !important;
        font-weight: 600 !important;
        line-height: 1.7 !important;
        color: #53575a !important;
        margin-bottom: 0.5rem !important;
    }

    /* Hero Section */
    .regen-hero {
        background: linear-gradient(135deg, #f5f5f5 0%, #ffffff 100%);
        padding: 3rem 2rem;
        border-radius: 5px;
        margin-bottom: 2rem;
        text-align: center;
        border: 1px solid #eaeaea;
    }

    .regen-hero-title {
        font-size: 48px;
        font-weight: 600;
        color: #53575a;
        margin-bottom: 1rem;
        font-family: 'Raleway', sans-serif;
        line-height: 1.7;
    }

    .regen-hero-subtitle {
        font-size: 20px;
        font-weight: 400;
        color: #53575a;
        margin-bottom: 0.5rem;
        font-family: 'Raleway', sans-serif;
        line-height: 1.7;
    }

    .regen-hero-accent {
        font-size: 17px;
        color: #e40032;
        font-weight: 600;
        font-family: 'Raleway', sans-serif;
    }

    /* Service Cards following brand design */
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

    .regen-card-icon {
        font-size: 50px;
        margin-bottom: 15px;
        display: block;
    }

    .regen-card-title {
        font-size: 20px;
        font-weight: 600;
        color: #53575a;
        margin-bottom: 15px;
        font-family: 'Raleway', sans-serif;
        line-height: 1.7;
    }

    .regen-card-text {
        font-size: 17px;
        font-weight: 400;
        color: #53575a;
        font-family: 'Raleway', sans-serif;
        line-height: 1.7;
    }

    /* Primary Button following brand style */
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
        text-decoration: none !important;
    }

    .regen-button:visited {
        color: #ffffff !important;
        text-decoration: none !important;
    }

    /* Table styling with gradient header */
    .regen-table {
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
        font-family: 'Raleway', sans-serif;
    }

    .regen-table thead {
        background: linear-gradient(to right, #eb4065, #e40032);
    }

    .regen-table th {
        color: #ffffff;
        font-size: 18px;
        font-weight: 700;
        padding: 15px;
        text-align: center;
        border: 1px solid #e40032;
    }

    .regen-table td {
        background: #EEEEEE;
        border: 1px solid #AAAAAA;
        padding: 10px 15px;
        text-align: center;
        font-size: 17px;
        font-weight: 400;
        color: #53575a;
        line-height: 1.5;
    }

    .regen-table tbody tr:nth-child(even) td {
        background: #ffffff;
    }

    .regen-table tfoot td {
        border-top: 4px solid #e40032;
        background: #ffffff;
        text-align: center;
        font-weight: 600;
        padding: 12px 15px;
    }

    /* Metric boxes */
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

    /* Content sections */
    .regen-section {
        background-color: #f5f5f5;
        padding: 30px 25px;
        border-radius: 5px;
        margin: 20px 0;
    }

    .regen-section-white {
        background-color: #ffffff;
        padding: 30px 25px;
        border-radius: 5px;
        margin: 20px 0;
        border: 1px solid #eaeaea;
    }

    /* Links following brand style */
    a, .regen-link {
        color: #e40032;
        text-decoration: none;
        transition: color 0.2s ease;
        font-weight: 400;
    }

    a:hover, .regen-link:hover {
        color: #3a3a3a;
        text-decoration: underline;
    }

    /* Dividers */
    .regen-divider {
        height: 1px;
        background-color: #dddddd;
        margin: 30px 0;
        border: none;
    }

    /* Accent text */
    .regen-accent {
        color: #e40032;
        font-weight: 600;
    }

    /* Footer */
    .regen-footer {
        background-color: #ffffff !important;
        color: #53575a;
        padding: 30px 20px;
        border-top: 4px solid #e40032;
        border-radius: 0;
        text-align: center;
        margin-top: 40px;
    }

    .regen-footer a {
        color: #e40032;
        text-decoration: none;
    }

    .regen-footer a:hover {
        color: #3a3a3a;
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

# Load paths
BASE_DIR = Path(__file__).resolve().parent.parent
DASHBOARD_DIR = Path(__file__).resolve().parent.parent
LOGO_PATH = DASHBOARD_DIR / 'assets' / 'regen_ag_lab_logo.png'
LOGO_TAGLINE_PATH = DASHBOARD_DIR / 'assets' / 'regen_logo_with_tagline.png'

# Header - Simple text-based, no oversized logo
st.markdown("""
<div style="text-align: center; padding: 2rem 1rem 1rem 1rem;">
    <h1 style="color: #e40032; margin: 0; font-size: 36px; font-weight: 600; font-family: 'Raleway', sans-serif;">
        Regen Ag Lab
    </h1>
    <p style="color: #53575a; margin: 0.5rem 0 0 0; font-size: 17px; font-family: 'Raleway', sans-serif;">
        Measuring Soil as a Living System
    </p>
</div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="regen-hero">
    <div class="regen-hero-title">Regen Ag Lab Brand Style Example</div>
    <div class="regen-hero-subtitle">Official Design System Implementation</div>
    <div class="regen-hero-accent">Demonstrating typography, colors, and components</div>
</div>
""", unsafe_allow_html=True)

# Introduction
st.markdown("""
<div class="regen-section-white">
<h3 class="regen-h3">About This Page</h3>
<p>This page demonstrates the proper implementation of the <span class="regen-accent">Regen Ag Lab brand style guide</span>.
All elements on this page follow the official design specifications from <a href="https://regenaglab.com/" target="_blank">regenaglab.com</a>.</p>

<p>The style guide includes specific requirements for:</p>
<ul>
<li><strong>Typography:</strong> Raleway font family with specific sizes and weights</li>
<li><strong>Color Palette:</strong> Brand red (#e40032), dark gray (#53575a), and supporting colors</li>
<li><strong>Components:</strong> Buttons, cards, tables, and interactive elements</li>
<li><strong>Layout:</strong> Spacing, containers, and responsive design patterns</li>
</ul>
</div>
""", unsafe_allow_html=True)

# Typography Examples
st.markdown("<hr class='regen-divider'>", unsafe_allow_html=True)
st.markdown("<h2 class='regen-h2'>Typography Scale</h2>", unsafe_allow_html=True)

st.markdown("""
<div class="regen-section">
<h1 class="regen-h1">H1: Main Page Heading (48px, Weight 600)</h1>
<h2 class="regen-h2">H2: Section Heading (42px, Weight 600)</h2>
<h3 class="regen-h3">H3: Subsection Heading (30px, Weight 600)</h3>
<h4 class="regen-h4">H4: Minor Heading (20px, Weight 600)</h4>
<p>Body Text: Regular paragraph text using 17px with line-height 1.7 for optimal readability.
The Raleway font family is used throughout for consistency with the Regen Ag Lab brand.</p>
<p><strong>Bold text uses weight 600</strong> for emphasis while maintaining readability.</p>
<p>Links appear in <a href="#">brand red (#e40032)</a> and transition to dark gray on hover.</p>
</div>
""", unsafe_allow_html=True)

# Color Palette
st.markdown("<hr class='regen-divider'>", unsafe_allow_html=True)
st.markdown("<h2 class='regen-h2'>Color Palette</h2>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div style="background: #e40032; padding: 40px 20px; border-radius: 5px; text-align: center; margin-bottom: 10px;">
        <span style="color: white; font-weight: 600;">Brand Red</span>
    </div>
    <div style="text-align: center; color: #53575a;">
        <strong>#e40032</strong><br>
        Primary accent, CTAs, links
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: #53575a; padding: 40px 20px; border-radius: 5px; text-align: center; margin-bottom: 10px;">
        <span style="color: white; font-weight: 600;">Dark Gray</span>
    </div>
    <div style="text-align: center; color: #53575a;">
        <strong>#53575a</strong><br>
        Body text, primary UI
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="background: #f5f5f5; padding: 40px 20px; border-radius: 5px; border: 1px solid #dddddd; text-align: center; margin-bottom: 10px;">
        <span style="color: #53575a; font-weight: 600;">Light Gray BG</span>
    </div>
    <div style="text-align: center; color: #53575a;">
        <strong>#f5f5f5</strong><br>
        Backgrounds, sections
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div style="background: #81d742; padding: 40px 20px; border-radius: 5px; text-align: center; margin-bottom: 10px;">
        <span style="color: white; font-weight: 600;">Green Accent</span>
    </div>
    <div style="text-align: center; color: #53575a;">
        <strong>#81d742</strong><br>
        Navigation, highlights
    </div>
    """, unsafe_allow_html=True)

# Metrics Display
st.markdown("<hr class='regen-divider'>", unsafe_allow_html=True)
st.markdown("<h2 class='regen-h2'>Metric Components</h2>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="regen-metric">
        <div class="regen-metric-value">3,625</div>
        <div class="regen-metric-label">Soil Samples</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="regen-metric">
        <div class="regen-metric-value">139</div>
        <div class="regen-metric-label">Variables Tracked</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="regen-metric">
        <div class="regen-metric-value">87%</div>
        <div class="regen-metric-label">Soil Health Focus</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="regen-metric">
        <div class="regen-metric-value">$32</div>
        <div class="regen-metric-label">Avg Savings/Sample</div>
    </div>
    """, unsafe_allow_html=True)

# Service Cards
st.markdown("<hr class='regen-divider'>", unsafe_allow_html=True)
st.markdown("<h2 class='regen-h2'>Service Card Components</h2>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="regen-card">
        <span class="regen-card-icon">🔬</span>
        <div class="regen-card-title">Soil Analysis</div>
        <div class="regen-card-text">Comprehensive testing using the Haney methodology to measure soil as a living system</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="regen-card">
        <span class="regen-card-icon">📊</span>
        <div class="regen-card-title">Data Insights</div>
        <div class="regen-card-text">Advanced analytics and visualization tools for understanding soil health patterns</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="regen-card">
        <span class="regen-card-icon">🌱</span>
        <div class="regen-card-title">Regenerative Practices</div>
        <div class="regen-card-text">Evidence-based recommendations for improving soil health and farm profitability</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="regen-card">
        <span class="regen-card-icon">💰</span>
        <div class="regen-card-title">Economic ROI</div>
        <div class="regen-card-text">Calculate cost savings from optimized fertilizer recommendations and soil health</div>
    </div>
    """, unsafe_allow_html=True)

# Button Examples
st.markdown("<hr class='regen-divider'>", unsafe_allow_html=True)
st.markdown("<h2 class='regen-h2'>Button Styles</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("""
    <div class="regen-section-white" style="text-align: center;">
        <h4 class="regen-h4">Primary Button (Hover to see effect)</h4>
        <p style="margin-bottom: 20px;">Default state: Dark gray (#53575a) | Hover state: Brand red (#e40032)</p>
        <a href="#" class="regen-button">View Services</a>
        <span style="margin: 0 10px;"></span>
        <a href="#" class="regen-button">Get Started</a>
        <span style="margin: 0 10px;"></span>
        <a href="#" class="regen-button">Learn More</a>
    </div>
    """, unsafe_allow_html=True)

# Table Example
st.markdown("<hr class='regen-divider'>", unsafe_allow_html=True)
st.markdown("<h2 class='regen-h2'>Table Component with Gradient Header</h2>", unsafe_allow_html=True)

st.markdown("""
<table class="regen-table">
    <thead>
        <tr>
            <th>Test Type</th>
            <th>Metrics Measured</th>
            <th>Turnaround Time</th>
            <th>Investment</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Haney Soil Health Test</strong></td>
            <td>CO2 Respiration, H3A Nutrients, WEOC/WEON, Soil Health Score</td>
            <td>7-10 days</td>
            <td>$55</td>
        </tr>
        <tr>
            <td><strong>Traditional Soil Test</strong></td>
            <td>NPK, pH, Cation Exchange, Basic Chemistry</td>
            <td>5-7 days</td>
            <td>$25</td>
        </tr>
        <tr>
            <td><strong>Complete Package</strong></td>
            <td>Haney + Traditional + Micronutrient Panel</td>
            <td>10-14 days</td>
            <td>$95</td>
        </tr>
        <tr>
            <td><strong>Plant Tissue Analysis</strong></td>
            <td>Macro & Micronutrients in Plant Material</td>
            <td>7-10 days</td>
            <td>$40</td>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <td colspan="4">All prices are per sample. Volume discounts available for 50+ samples.</td>
        </tr>
    </tfoot>
</table>
""", unsafe_allow_html=True)

# Content Sections
st.markdown("<hr class='regen-divider'>", unsafe_allow_html=True)
st.markdown("<h2 class='regen-h2'>Content Sections</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="regen-section">
        <h3 class="regen-h3">Gray Background Section</h3>
        <p>This section uses the light gray background (#f5f5f5) for visual separation and hierarchy.
        It's ideal for secondary content, callouts, or featured information.</p>
        <p>The 30px padding and 5px border radius maintain consistency with the brand's clean,
        modern aesthetic.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="regen-section-white">
        <h3 class="regen-h3">White Background Section</h3>
        <p>This section uses white background with a subtle border for emphasis. It's perfect for
        primary content areas and important information that needs to stand out.</p>
        <p>The border uses the brand's light gray (#eaeaea) to create definition without being
        visually heavy.</p>
    </div>
    """, unsafe_allow_html=True)

# Key Findings Section
st.markdown("<hr class='regen-divider'>", unsafe_allow_html=True)
st.markdown("<h2 class='regen-h2'>Using Brand Elements in Context</h2>", unsafe_allow_html=True)

st.markdown("""
<div class="regen-section-white">
<h3 class="regen-h3">The Haney Soil Health Test Advantage</h3>

<p>The <span class="regen-accent">Haney Soil Health Test</span> represents a paradigm shift in agricultural
soil testing. Unlike traditional methods that treat soil as an inert substrate, the Haney Test measures soil
as a <strong>living, dynamic ecosystem</strong>.</p>

<h4 class="regen-h4">Key Methodology Components:</h4>

<p><strong>24-Hour CO2-C Respiration:</strong><br>
Measures biological activity by quantifying carbon dioxide released by soil microbes. Higher respiration equals
more active, healthier soil biology.</p>

<p><strong>H3A Extractant:</strong><br>
Uses weak organic acids that mimic plant root exudates, providing more accurate plant-available nutrient
measurements than harsh chemical extractants used in traditional testing.</p>

<p><strong>WEOC/WEON (Water-Extractable Organic C/N):</strong><br>
Measures readily available carbon and nitrogen that fuel soil microbial communities - the "food web" that
drives nutrient cycling.</p>

<p><strong>Integrated Soil Health Score:</strong><br>
Combines biological and chemical data into a single metric that reflects overall soil ecosystem function.</p>

<div style="margin-top: 25px; text-align: center;">
    <a href="https://regenaglab.com/services/soil-analysis/" target="_blank" class="regen-button">
        Learn More About Our Services
    </a>
</div>
</div>
""", unsafe_allow_html=True)

# Design Guidelines
st.markdown("<hr class='regen-divider'>", unsafe_allow_html=True)
st.markdown("<h2 class='regen-h2'>Style Guide Implementation Notes</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="regen-section">
    <h4 class="regen-h4">Typography Standards</h4>
    <ul style="margin: 0; padding-left: 20px;">
        <li><strong>Font Family:</strong> Raleway (Google Fonts)</li>
        <li><strong>Base Size:</strong> 17px (larger than standard 16px)</li>
        <li><strong>Line Height:</strong> 1.7 for optimal readability</li>
        <li><strong>Weights Used:</strong> 400 (normal), 600 (semibold), 700 (bold)</li>
        <li><strong>Body Color:</strong> Dark gray #53575a</li>
    </ul>
    </div>

    <div class="regen-section" style="margin-top: 20px;">
    <h4 class="regen-h4">Color Usage Guidelines</h4>
    <ul style="margin: 0; padding-left: 20px;">
        <li><strong>Brand Red:</strong> CTAs, links, accents, hover states</li>
        <li><strong>Dark Gray:</strong> Primary text, default button state</li>
        <li><strong>Light Gray:</strong> Backgrounds, section divisions</li>
        <li><strong>White:</strong> Content areas, contrast elements</li>
        <li><strong>Green:</strong> Active states, success indicators</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="regen-section">
    <h4 class="regen-h4">Component Specifications</h4>
    <ul style="margin: 0; padding-left: 20px;">
        <li><strong>Border Radius:</strong> 5px consistent across all components</li>
        <li><strong>Button Padding:</strong> 16px vertical × 35px horizontal</li>
        <li><strong>Card Padding:</strong> 30px vertical × 25px horizontal</li>
        <li><strong>Section Spacing:</strong> 20-30px between elements</li>
        <li><strong>Transitions:</strong> 0.3s ease for hover effects</li>
    </ul>
    </div>

    <div class="regen-section" style="margin-top: 20px;">
    <h4 class="regen-h4">Responsive Design</h4>
    <ul style="margin: 0; padding-left: 20px;">
        <li><strong>Max Width:</strong> 1240px for content containers</li>
        <li><strong>Small:</strong> 544px (mobile, single column)</li>
        <li><strong>Medium:</strong> 768px (tablet, 2 columns)</li>
        <li><strong>Large:</strong> 921px+ (desktop, 4 columns)</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("<hr class='regen-divider'>", unsafe_allow_html=True)

# Convert logo to base64 for embedding in HTML
import base64

try:
    with open(LOGO_PATH, "rb") as img_file:
        logo_base64 = base64.b64encode(img_file.read()).decode()
    logo_html = f'<img src="data:image/png;base64,{logo_base64}" style="width: 150px; height: auto;" alt="Regen Ag Lab Logo">'
except:
    logo_html = ""

# Footer with embedded logo - all in one HTML block
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
