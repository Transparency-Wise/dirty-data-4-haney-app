# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an **Agricultural Soil Health EDA Project** analyzing 300 soil test CSV files (3,625 samples, 139 variables) with comprehensive exploratory data analysis, visualizations, and an interactive Streamlit dashboard.

**Key Focus Areas:**
- Soil health metrics analysis
- Nutrient availability assessment
- Cover crop impact evaluation
- Traditional vs Haney testing methodology comparison
- Economic analysis of testing approaches

## Repository Structure

```
agwise-gh/
├── agwise_eda/                    # Main project directory
│   ├── data/
│   │   ├── raw/                   # Original 300 CSV files
│   │   │   └── OneDrive_1_10-5-2025/
│   │   └── processed/             # Combined/cleaned datasets
│   │       └── combined_soil_data.csv (3,625 × 139)
│   │
│   ├── scripts/                   # Analysis pipeline (5 scripts)
│   │   ├── run_all_analyses.py   # Master orchestration script
│   │   ├── 01_eda_analysis.py
│   │   ├── 02_eda_visualizations.py
│   │   ├── 03_eda_correlations.py
│   │   ├── 04_eda_categorical_crops.py
│   │   └── 05_eda_advanced_insights.py
│   │
│   ├── dashboard/                 # Streamlit interactive dashboard
│   │   ├── app.py                # Main dashboard application
│   │   └── pages/
│   │       └── 02_Economic_Analysis.py
│   │
│   ├── outputs/
│   │   ├── visualizations/       # 15 high-resolution PNG plots
│   │   └── tables/               # 11 CSV summary tables
│   │
│   ├── reports/                   # Analysis documentation
│   │   ├── COMPREHENSIVE_EDA_REPORT.md
│   │   └── EXECUTIVE_SUMMARY_FULL_DATASET.md
│   │
│   ├── docs/                      # Supporting documentation
│   │   ├── METHODOLOGY.md
│   │   └── ECONOMIC_MODEL_DOCUMENTATION.md
│   │
│   ├── feedback/                  # User feedback system
│   │   ├── user_feedback.csv     # Feedback entries
│   │   └── uploads/              # User-submitted files
│   │
│   └── requirements.txt
│
└── [root level scripts]           # Legacy/standalone analysis scripts
    ├── full_eda_pipeline.py
    ├── generate_pdf_report.py
    └── generate_presentation.py
```

## Common Development Tasks

### Setting Up Environment

```bash
# Navigate to project
cd agwise_eda

# Create and activate virtual environment
python3 -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running Analysis Pipeline

```bash
# Run complete analysis pipeline
cd agwise_eda/scripts
python run_all_analyses.py

# Run individual analysis scripts
python 01_eda_analysis.py
python 02_eda_visualizations.py
# ... etc
```

**Expected Runtime:** ~3-5 minutes for full pipeline

**Outputs Generated:**
- Visualizations: `agwise_eda/outputs/visualizations/`
- Tables: `agwise_eda/outputs/tables/`
- Reports: `agwise_eda/reports/`

### Running Dashboard

```bash
# From agwise_eda directory
streamlit run dashboard/app.py

# Dashboard opens at: http://localhost:8501 (or 8502, 8503, etc.)
```

**Dashboard Features:**
- Interactive data exploration
- Soil health analysis
- Economic impact calculator
- Geographic mapping (ZIP code-based)
- User feedback system (submissions saved to `feedback/`)

### Working with Data

**Primary Dataset:**
- Location: `agwise_eda/data/processed/combined_soil_data.csv`
- Shape: 3,625 rows × 139 columns
- Key Variables: 125 numeric, 14 categorical

**Important Data Notes:**
- 46% duplicate rate (flagged but not removed - requires investigation)
- High missing data in crop recommendations (>95%)
- Enzyme measurements 100% missing
- No geographic coordinates available

**Loading Data in Scripts:**
```python
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / 'data' / 'processed' / 'combined_soil_data.csv'
df = pd.read_csv(DATA_FILE)
```

## Code Architecture

### Analysis Pipeline Pattern

All analysis scripts follow this structure:

```python
# 1. Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Path setup
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / 'data' / 'processed' / 'combined_soil_data.csv'
OUTPUT_DIR = BASE_DIR / 'outputs'

# 3. Load data
df = pd.read_csv(DATA_FILE)

# 4. Analysis logic
# ... perform analysis ...

# 5. Save outputs
plt.savefig(OUTPUT_DIR / 'visualizations' / 'plot.png', dpi=300, bbox_inches='tight')
results_df.to_csv(OUTPUT_DIR / 'tables' / 'results.csv', index=False)

# 6. Print summary
print(f"✓ Analysis complete")
```

**Key Patterns:**
- Use `pathlib.Path` for cross-platform path handling
- Save all plots at 300 DPI with tight bounding boxes
- Use descriptive filenames with underscores (e.g., `soil_health_by_cover_crop.csv`)
- Print completion messages with timing information

### Dashboard Architecture

**Main App:** `dashboard/app.py`
- Streamlit multi-page application
- Sidebar navigation with filters
- Cached data loading with `@st.cache_data`
- Plotly for interactive visualizations
- Feedback system integrated in sidebar

**Page Pattern:**
```python
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Page Name", page_icon="🌱", layout="wide")

# Load data (cached)
@st.cache_data
def load_data():
    return pd.read_csv(DATA_FILE)

df = load_data()

# Layout
col1, col2 = st.columns(2)

with col1:
    st.metric("Metric Name", value)

with col2:
    fig = px.scatter(df, x='var1', y='var2')
    st.plotly_chart(fig, use_container_width=True)
```

### Feedback System

User feedback is automatically collected via the dashboard sidebar:

**Storage:**
- CSV database: `agwise_eda/feedback/user_feedback.csv`
- File uploads: `agwise_eda/feedback/uploads/`

**Data Captured:**
- Timestamp
- Page context
- Feedback type (Question, Bug Report, Feature Request, etc.)
- Message text
- Optional file attachments

**Reviewing Feedback:**
```python
import pandas as pd

feedback = pd.read_csv('agwise_eda/feedback/user_feedback.csv')
print(feedback.tail(10))  # View recent feedback
print(feedback['type'].value_counts())  # Summary by type
```

## Key Technical Decisions

### Statistical Methods

**Correlation Analysis:**
- Pearson correlation used (assumes linear relationships)
- Threshold: |r| > 0.5 for "strong" correlations
- Full correlation matrix computed for 27 key soil health variables

**Outlier Detection:**
- IQR method: Q1 - 1.5×IQR to Q3 + 1.5×IQR
- Outliers identified but NOT removed (may be legitimate high performers)

**Missing Data:**
- No imputation performed
- Complete case analysis (listwise deletion)
- High missing rates (>50%) documented

**Visualization:**
- Matplotlib + Seaborn for static plots
- Plotly for interactive dashboard charts
- 300 DPI for all saved figures

### Data Versioning

Multiple versions of combined data exist:
- `combined_soil_data.csv` - Primary version
- `combined_soil_data_FULL.csv` - Full version (dashboard uses this)

When working with data, verify which version is appropriate for the analysis context.

## Known Issues and Limitations

1. **Duplicate Samples (46%):** Requires investigation with laboratory to understand whether these are:
   - Temporal duplicates (same field, different dates)
   - Spatial duplicates (same field, different locations)
   - Data artifacts

2. **Missing Geographic Data:** No latitude/longitude coordinates available
   - Dashboard uses ZIP code geocoding as workaround
   - Requires `uszipcode` package

3. **High Missing Data:** Crop recommendations >95% missing, enzyme measurements 100% missing

4. **No Temporal Information:** Limited date tracking across samples

## Important Findings to Preserve

**Critical Soil Health Drivers:**
- Soil respiration: r=0.952 (strongest predictor)
- Organic matter: r=0.871
- Alkaline pH: r=-0.726 (negative impact)

**Economic Impact:**
- Haney vs Traditional testing: +32.4 lbs/A nitrogen difference
- Potential savings: $31.95 per sample
- Total dataset savings potential: $51,113.57

**Cover Crop Patterns:**
- Grass-dominant mixes (20-40% legume) show highest soil health
- Legume-dominant mixes (60-70% legume) show lowest scores
- Finding requires statistical validation

**Soil Characteristics:**
- 87% of soils rate "Poor" to "Fair" in health
- 90% alkaline (pH >7.5) - indicates regional pattern
- Nitrogen most limiting nutrient

## Testing and Validation

### Running Tests

Currently no automated test suite. When adding tests:

```bash
# Standard pattern
pytest tests/

# With coverage
pytest --cov=agwise_eda tests/
```

### Manual Validation

```bash
# Verify data pipeline
cd agwise_eda/scripts
python run_all_analyses.py

# Check outputs exist
ls -lh ../outputs/visualizations/
ls -lh ../outputs/tables/

# Verify dashboard
streamlit run dashboard/app.py
# Navigate to all pages, check for errors
```

## Python Environment Specifications

**Required Python:** 3.13+

**Core Dependencies:**
```
pandas==2.3.3
numpy==2.3.3
scipy==1.16.2
matplotlib==3.10.6
seaborn==0.13.2
streamlit>=1.28.0
plotly>=5.18.0
uszipcode>=1.0.1,<2.0
sqlalchemy>=1.4.0,<2.0
```

**Note:** SQLAlchemy version pinned to <2.0 for uszipcode compatibility

## Next Steps for Development

### Immediate Priorities
1. Resolve duplicate sample logic with laboratory
2. Add statistical significance testing to key findings
3. Validate Traditional vs Haney comparison methodology
4. Add geographic coordinates to dataset

### Medium-term Enhancements
1. Implement predictive modeling (Random Forest, XGBoost)
2. Add cluster analysis for soil type identification
3. Statistical validation of cover crop findings
4. Expand dashboard with additional pages

### Long-term Goals
1. Temporal data collection protocol
2. Geographic expansion of dataset
3. Management intervention trials
4. Automated report generation

## Documentation References

**Key Files:**
- Project overview: `agwise_eda/README.md`
- Comprehensive findings: `agwise_eda/reports/COMPREHENSIVE_EDA_REPORT.md`
- Statistical methods: `agwise_eda/docs/METHODOLOGY.md`
- Economic model: `agwise_eda/docs/ECONOMIC_MODEL_DOCUMENTATION.md`
- Feedback system: `agwise_eda/FEEDBACK_SYSTEM.md`
- Data dictionary: `agwise_eda/DATA_DICTIONARY.md`

**External Resources:**
- Haney Test methodology: `Haney Test Explained - Lance.pdf`
- Interpretation guide: `Haney-Interpretations - Ward.pdf`

## Working with Claude Code

When making changes to this repository:

1. **Preserve Data Integrity:** Never modify files in `data/raw/`
2. **Follow Naming Conventions:** Use lowercase with underscores (e.g., `soil_health_analysis.py`)
3. **Update Documentation:** Keep markdown files synchronized with code changes
4. **Maintain Pipeline:** Ensure `run_all_analyses.py` reflects all scripts
5. **Test Dashboard:** Always verify Streamlit app after modifications to `dashboard/`
6. **Document Decisions:** Add comments explaining non-obvious statistical choices

**When Adding New Analysis Scripts:**
1. Place in `agwise_eda/scripts/`
2. Follow numbered naming (e.g., `06_new_analysis.py`)
3. Add to `run_all_analyses.py` pipeline
4. Save outputs to appropriate directories
5. Update documentation

**When Modifying Dashboard:**
1. Test with `streamlit run dashboard/app.py`
2. Verify feedback system still works
3. Check all pages load correctly
4. Ensure caching works properly
5. Validate plotly interactive charts

## Project Status

**Status:** ✅ Complete and production-ready

**Last Major Update:** October 5-6, 2025

**Version:** 1.0

**Deliverables:** 32+ files including reports, scripts, visualizations, and documentation
