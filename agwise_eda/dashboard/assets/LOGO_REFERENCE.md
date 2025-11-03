# Regen Ag Lab Logo Assets

**Downloaded:** October 31, 2025
**Source:** https://regenaglab.com/

---

## 📁 Available Logo Files

### 1. Main Header Logo (with Tagline)
- **Filename:** `regen_logo_with_tagline.png`
- **Dimensions:** 222 × 75 pixels
- **Size:** 11 KB
- **Format:** PNG
- **Background:** Transparent
- **Usage:** Primary header logo, includes tagline
- **Best For:** Website headers, main navigation, documents
- **Source URL:** https://regenaglab.com/wp-content/uploads/2020/02/Regen_Logo-With-Tagline_Screen-222x75.png

### 2. Reversed/Footer Logo
- **Filename:** `regen_logo_reversed.png`
- **Dimensions:** 300 × 151 pixels
- **Size:** 17 KB
- **Format:** PNG
- **Background:** Transparent (white logo for dark backgrounds)
- **Usage:** Footer sections, dark backgrounds, inverted themes
- **Best For:** Dark mode, footer sections, reversed color schemes
- **Source URL:** https://regenaglab.com/wp-content/uploads/2019/12/Regen_Logo_Reversed-Screen-300x151.png

### 3. Icon/Favicon
- **Filename:** `regen_icon_50x50.png`
- **Dimensions:** 50 × 50 pixels
- **Size:** 788 bytes
- **Format:** PNG
- **Background:** Transparent
- **Usage:** Favicon, small icons, service cards
- **Best For:** Browser tabs, small UI elements, mobile icons
- **Source URL:** https://regenaglab.com/wp-content/uploads/2020/02/growth-50x50-1.png

### 4. Original Logo (User Provided)
- **Filename:** `regen_ag_lab_logo.png`
- **Dimensions:** Variable
- **Size:** 12 KB
- **Format:** PNG
- **Usage:** General purpose logo
- **Best For:** Flexible usage across dashboard

---

## 🎨 Logo Usage Guidelines

### Color Versions
- **Standard Logo:** Use on white or light backgrounds (#f5f5f5 or lighter)
- **Reversed Logo:** Use on dark backgrounds (#53575a or darker)

### Size Recommendations

#### Desktop/Web
- **Header:** 150-222px width (maintain aspect ratio)
- **Footer:** 200-300px width
- **Sidebar:** 100-150px width
- **Icon/Favicon:** 50×50px (no scaling needed)

#### Mobile/Responsive
- **Header:** 120-180px width
- **Footer:** 150-200px width
- **Collapsed Navigation:** 80-100px width

### Spacing & Clearance
- **Minimum Clearance:** Leave at least 20px of space around logo on all sides
- **Alignment:** Center-align for hero sections, left-align for headers
- **Never:** Stretch, distort, or change aspect ratio

---

## 💻 Implementation Examples

### Streamlit Dashboard Header
```python
from PIL import Image
from pathlib import Path

# Load logo
LOGO_PATH = Path(__file__).parent / 'assets' / 'regen_logo_with_tagline.png'
logo = Image.open(LOGO_PATH)

# Display in header
col1, col2, col3 = st.columns([1, 3, 1])
with col1:
    st.image(logo, width=150)
```

### HTML/CSS Implementation
```html
<!-- Standard Logo -->
<img src="assets/regen_logo_with_tagline.png"
     alt="Regen Ag Lab"
     style="max-width: 222px; height: auto;">

<!-- Footer Reversed Logo -->
<img src="assets/regen_logo_reversed.png"
     alt="Regen Ag Lab"
     style="max-width: 250px; height: auto;">

<!-- Favicon -->
<link rel="icon" type="image/png"
      href="assets/regen_icon_50x50.png"
      sizes="50x50">
```

### Responsive CSS
```css
.logo-header {
  max-width: 222px;
  height: auto;
}

@media (max-width: 768px) {
  .logo-header {
    max-width: 150px;
  }
}

@media (max-width: 544px) {
  .logo-header {
    max-width: 120px;
  }
}
```

---

## 📐 Logo Specifications

### Aspect Ratios
- **With Tagline:** ~2.96:1 (222:75)
- **Reversed Logo:** ~1.99:1 (300:151)
- **Icon:** 1:1 (50:50)

### File Formats
- **Current:** PNG (transparent background)
- **Recommended:** Keep PNG for web use
- **Alternative:** SVG would be ideal for scalability (not currently available)

### Color Information
Based on the website analysis:
- **Primary Red:** #e40032
- **Dark Gray:** #53575a
- **Logo likely uses these brand colors**

---

## 🔄 Logo Selection Guide

| Use Case | Recommended Logo | Size |
|----------|-----------------|------|
| Dashboard Header (Light BG) | `regen_logo_with_tagline.png` | 150-180px |
| Dashboard Footer (Dark BG) | `regen_logo_reversed.png` | 200-250px |
| Sidebar Navigation | `regen_logo_with_tagline.png` | 120-150px |
| Browser Tab/Favicon | `regen_icon_50x50.png` | 50×50px |
| Mobile Header | `regen_logo_with_tagline.png` | 100-120px |
| Print Materials | `regen_logo_with_tagline.png` | Full resolution |
| Social Media Profile | `regen_icon_50x50.png` | Scale to platform requirements |
| Loading Screen | `regen_logo_with_tagline.png` | 200-300px |

---

## ⚠️ Don'ts

- ❌ Don't change the logo colors
- ❌ Don't add effects (drop shadows, glows, etc.) without approval
- ❌ Don't rotate or skew the logo
- ❌ Don't place logo on busy backgrounds that reduce readability
- ❌ Don't use the standard logo on dark backgrounds (use reversed version)
- ❌ Don't use the reversed logo on light backgrounds (use standard version)
- ❌ Don't crop or cut off parts of the logo
- ❌ Don't rearrange logo elements

---

## 📝 Notes

### Current Dashboard Usage
- **app.py:** Uses original `regen_ag_lab_logo.png` in header (150px width)
- **01_Home.py:** Uses original logo, centered below hero section
- **Future:** Consider switching to `regen_logo_with_tagline.png` for better branding

### Recommended Updates
1. Replace header logo with `regen_logo_with_tagline.png` for professional appearance
2. Use `regen_logo_reversed.png` in footer sections
3. Set `regen_icon_50x50.png` as page favicon
4. Maintain consistent sizing across all pages

### Accessibility
- Always include `alt="Regen Ag Lab"` or descriptive alt text
- Ensure sufficient contrast with background colors
- Provide text fallback if image fails to load

---

*Logo assets downloaded from Regen Ag Lab official website (regenaglab.com) for use in partnership dashboard project.*
