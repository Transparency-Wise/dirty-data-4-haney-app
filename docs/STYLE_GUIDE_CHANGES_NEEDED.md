# Style Guide Compliance Changes Needed

**Project:** Haney Soil AI Dashboard
**Reference:** REGEN_AG_LAB_STYLE_GUIDE.md
**Date:** Current Session
**Status:** Pending Implementation

---

## 🎯 Overview

This document outlines the specific changes needed to bring the Haney Soil AI dashboard into full compliance with the official Regen Ag Lab brand style guide.

---

## 🔴 Changes Required

### 1. Icon Sizing (Home Page)

**Location:** `pages/01_Home.py`
**CSS Class:** `.feature-icon`

**Current:**
```css
.feature-icon {
    font-size: 60px;
    margin-bottom: 20px;
    display: block;
}
```

**Required per Style Guide:**
- Icon size: **50x50px**

**Fix:**
```css
.feature-icon {
    font-size: 50px;  /* Changed from 60px */
    margin-bottom: 15px;  /* Reduced to match guide */
    display: block;
}
```

**Priority:** Medium
**Impact:** Visual consistency with official website

---

### 2. Service Card Padding (Home Page)

**Location:** `pages/01_Home.py`
**CSS Class:** `.feature-card`

**Current:**
```css
.feature-card {
    padding: 40px 30px;
    /* ... */
}
```

**Required per Style Guide:**
- Card padding: **20-25px internal padding**

**Fix:**
```css
.feature-card {
    padding: 25px 20px;  /* Changed from 40px 30px */
    /* ... */
}
```

**Priority:** Medium
**Impact:** Tighter, more professional card appearance

---

### 3. Button Line Height

**Location:** All pages
**CSS Class:** `.regen-button`

**Current:**
```css
.regen-button {
    /* line-height not explicitly set */
}
```

**Required per Style Guide:**
- Button text line-height: **1.0**

**Fix:**
```css
.regen-button {
    background-color: #53575a;
    color: #ffffff !important;
    font-family: 'Raleway', sans-serif;
    font-size: 16px;
    font-weight: 600;
    padding: 16px 35px;
    border-radius: 5px;
    line-height: 1.0;  /* ADD THIS */
    /* ... */
}
```

**Priority:** Low
**Impact:** Consistent button text spacing

---

### 4. Container Max Width

**Location:** All pages
**Issue:** Max-width not enforced globally

**Required per Style Guide:**
- Desktop max width: **1240px**
- Should apply to main content areas

**Fix:**

Add to main CSS:
```css
.main .block-container {
    max-width: 1240px !important;
    margin: 0 auto !important;
}
```

**Priority:** High
**Impact:** Proper content width constraints on large screens

---

### 5. Section Spacing Standardization

**Location:** All pages
**Issue:** Inconsistent spacing between sections

**Current:**
- Various: `1rem`, `1.5rem`, `40px`, `margin-top: 40px`

**Required per Style Guide:**
- Section margin: **15-30px between major sections**
- Spacing unit: **15px base**

**Fix:**

Standardize all section margins:
```css
/* Section dividers */
.section-spacing {
    margin: 30px 0;  /* 2x spacing unit */
}

/* Between major sections */
hr, .divider {
    margin: 30px 0;
}
```

**Priority:** Medium
**Impact:** Visual consistency and rhythm

---

### 6. Card Hover Animation Timing

**Location:** Home page and app.py
**CSS Classes:** `.feature-card`, `.stats-highlight`, `.regen-card`

**Current:**
```css
.feature-card {
    transition: all 0.3s ease;
}

.feature-card:hover {
    box-shadow: 0 6px 20px rgba(228, 0, 50, 0.2);
    transform: translateY(-5px);
}
```

**Required per Style Guide:**
- Shadow effects: **0.2s ease** (not 0.3s)
- Button hover: 0.3s ease (keep as is)

**Fix:**
```css
.feature-card {
    transition: all 0.2s ease;  /* Changed from 0.3s */
}

.stats-highlight {
    transition: all 0.2s ease;  /* Changed from 0.3s */
}

.regen-card {
    transition: all 0.2s ease;  /* Changed from 0.3s */
}

/* Keep button transitions at 0.3s */
.regen-button {
    transition: background-color 0.3s ease;  /* Unchanged */
}
```

**Priority:** Low
**Impact:** Snappier, more responsive feel

---

### 7. Responsive Breakpoints Documentation

**Location:** All CSS files
**Issue:** Breakpoints not explicitly documented

**Required per Style Guide:**
- Small: **544px**
- Medium: **768px**
- Large: **921px**

**Fix:**

Add CSS comments and media queries:
```css
/* Responsive Breakpoints per Regen Ag Lab Style Guide */
/* Small: 544px | Medium: 768px | Large: 921px */

@media (max-width: 544px) {
    /* Mobile styles */
}

@media (min-width: 544px) and (max-width: 921px) {
    /* Tablet styles */
}

@media (min-width: 921px) {
    /* Desktop styles */
}
```

**Priority:** Low (future enhancement)
**Impact:** Better mobile experience

---

### 8. CSS Variables Implementation

**Location:** All pages
**Issue:** Not using CSS custom properties consistently

**Required per Style Guide:**
```css
:root {
    --color-primary: #e40032;
    --color-dark: #53575a;
    --color-light-bg: #f5f5f5;
    --color-white: #ffffff;
    --color-green: #81d742;
    --font-family: 'Raleway', sans-serif;
    --font-size-base: 17px;
    --font-weight-normal: 400;
    --font-weight-semibold: 600;
    --border-radius: 5px;
    --spacing-unit: 15px;
}
```

**Fix:**

Already partially implemented. Ensure all hardcoded values reference variables:
```css
/* Instead of: */
color: #e40032;

/* Use: */
color: var(--color-primary);
```

**Priority:** Medium (maintenance benefit)
**Impact:** Easier theme updates

---

## ✅ Already Compliant

The following elements are correctly implemented per the style guide:

### Typography
- ✅ Raleway font family throughout
- ✅ H1: 48px, weight 600
- ✅ H2: 42px, weight 600
- ✅ H3: 30px, weight 600
- ✅ H4: 20px, weight 600
- ✅ Body: 17px, weight 400
- ✅ Line height: 1.7 for readability
- ✅ Button text: 16px, weight 600

### Colors
- ✅ Brand red: #e40032
- ✅ Dark gray text: #53575a
- ✅ Light gray background: #f5f5f5
- ✅ White: #ffffff
- ✅ Links: Red with hover to dark gray

### Components
- ✅ Button padding: 16px 35px
- ✅ Button hover: Gray → Red transition
- ✅ Border radius: 5px throughout
- ✅ Table gradient headers: #eb4065 to #e40032
- ✅ Table header: 18px, weight 700, white text
- ✅ Table body: 17px, alternating rows (#EEEEEE / white)
- ✅ Footer: Red top border (4px solid)

---

## 📊 Implementation Priority

### High Priority (Do First)
1. Container max width (1240px)
2. Section spacing standardization

### Medium Priority (Do Second)
1. Service card padding adjustment
2. Icon sizing correction
3. CSS variables consistency
4. Card hover timing adjustments

### Low Priority (Nice to Have)
1. Button line height
2. Responsive breakpoints documentation
3. Mobile optimization

---

## 🎨 Navigation Changes (New Requirement)

### Current Implementation
- **Style:** Sidebar navigation (Streamlit default)
- **Position:** Left side, collapsible
- **Analysis views:** Radio buttons in sidebar
- **Feedback:** Expandable section in sidebar

### Proposed Changes per Style Guide

**Navigation Style per Guide:**
- **Style:** Fixed/sticky top navigation
- **Background:** White or transparent default
- **Sticky behavior:** Green (#81d742) background on scroll
- **Mobile:** Hamburger menu at 921px breakpoint

**Required Implementation:**
1. **Top Navigation Bar**
   - Horizontal menu bar at top of page
   - Sticky/fixed positioning
   - Analysis views in dropdown menu
   - Feedback button in navbar

2. **Structure:**
   ```
   [Haney Soil AI Logo] [Home] [Analysis ▼] [About] [Feedback]
   ```

3. **Dropdown for Analysis Views:**
   - Overview & Statistics
   - Soil Health Analysis
   - Cover Crop Analysis
   - Economic Analysis
   - Correlation Explorer
   - Custom Analysis
   - Data Dictionary
   - Project Deliverables

4. **Challenges with Streamlit:**
   - Streamlit doesn't have native top navigation
   - Would require custom HTML/CSS/JavaScript
   - May conflict with Streamlit's page routing
   - Consider using `st.columns()` to simulate navbar
   - Or use `streamlit-option-menu` package

**Recommendation:**
Investigate `streamlit-option-menu` package which provides horizontal navigation that matches the style guide better than default sidebar.

---

## 📝 Implementation Checklist

- [ ] Update icon sizing to 50px
- [ ] Adjust card padding to 25px 20px
- [ ] Add button line-height: 1.0
- [ ] Implement max-width: 1240px constraint
- [ ] Standardize section spacing to 30px
- [ ] Update card hover transitions to 0.2s
- [ ] Document responsive breakpoints
- [ ] Refactor to use CSS variables consistently
- [ ] Investigate top navigation implementation
- [ ] Create horizontal menu bar
- [ ] Add analysis dropdown menu
- [ ] Move feedback button to navbar
- [ ] Test on mobile (< 921px)
- [ ] Verify all changes on each page:
  - [ ] app.py (main dashboard)
  - [ ] pages/01_Home.py
  - [ ] pages/02_Economic_Analysis.py
  - [ ] pages/03_Regen_Lab_Example.py

---

## 🔧 Technical Notes

### Streamlit Navigation Limitations

**Default Sidebar Approach:**
- Pros: Native Streamlit functionality, easy to implement
- Cons: Doesn't match style guide (top nav requirement)

**Custom Top Nav Options:**

1. **Pure CSS/HTML Approach:**
   - Use `st.markdown()` with custom HTML/CSS
   - Simulate top nav with styled links
   - Limited interactivity

2. **streamlit-option-menu Package:**
   - Third-party package
   - Provides horizontal menu bar
   - Closer to style guide requirements
   - Installation: `pip install streamlit-option-menu`

3. **Hybrid Approach:**
   - Keep Streamlit pages for routing
   - Add visual top nav with CSS
   - Use session state for page tracking

**Recommended Solution:**
Implement `streamlit-option-menu` with horizontal orientation to match Regen Ag Lab style guide while maintaining Streamlit's functionality.

---

## 📚 References

- **Style Guide:** `REGEN_AG_LAB_STYLE_GUIDE.md`
- **Official Website:** https://regenaglab.com/
- **Services Page:** https://regenaglab.com/services/soil-analysis/
- **Streamlit Docs:** https://docs.streamlit.io/
- **Option Menu Package:** https://github.com/victoryhb/streamlit-option-menu

---

## ✅ Approval & Sign-off

- [ ] Changes reviewed by project lead
- [ ] Style guide compliance verified
- [ ] Navigation changes approved
- [ ] Implementation timeline agreed
- [ ] Testing plan established

---

*Document created: Current session*
*Last updated: Current session*
*Status: Pending implementation*
