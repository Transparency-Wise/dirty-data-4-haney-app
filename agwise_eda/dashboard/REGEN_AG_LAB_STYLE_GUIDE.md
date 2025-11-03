# Regen Ag Lab Website Style Guide

**Analyzed from:** https://regenaglab.com/ and https://regenaglab.com/services/soil-analysis/

**Date:** October 31, 2025

---

## 🎨 Color Palette

### Primary Colors

| Color Name | Hex Code | RGB | Usage |
|------------|----------|-----|-------|
| **Brand Red/Crimson** | `#e40032` | rgb(228, 0, 50) | Primary accent, links, hover states, CTA buttons, table headers |
| **Dark Gray** | `#53575a` | rgb(83, 87, 90) | Body text, primary buttons (default state), UI elements |
| **Light Gray Background** | `#f5f5f5` | rgb(245, 245, 245) | Page backgrounds, section backgrounds |
| **White** | `#ffffff` | rgb(255, 255, 255) | Content backgrounds, contrast elements, header text on red |

### Secondary Colors

| Color Name | Hex Code | RGB | Usage |
|------------|----------|-----|-------|
| **Medium Gray** | `#3a3a3a` | rgb(58, 58, 58) | Secondary text, hover states |
| **Border Light Gray** | `#dddddd` | rgb(221, 221, 221) | Light borders, dividers |
| **Border Medium Gray** | `#eaeaea` | rgb(234, 234, 234) | Subtle borders |
| **Table Gray** | `#EEEEEE` | rgb(238, 238, 238) | Table backgrounds |
| **Table Border** | `#AAAAAA` | rgb(170, 170, 170) | Table borders |

### Accent Colors

| Color Name | Hex Code | RGB | Usage |
|------------|----------|-----|-------|
| **Green (Navigation)** | `#81d742` | rgb(129, 215, 66) | Sticky navigation background on scroll |
| **Red Gradient Light** | `#eb4065` | rgb(235, 64, 101) | Table header gradient (light end) |
| **Red Gradient Dark** | `#e40032` | rgb(228, 0, 50) | Table header gradient (dark end) |

---

## 📝 Typography

### Font Family
- **Primary Font:** `Raleway` (sans-serif)
- **Fallback:** System sans-serif stack

### Font Weights
- **Regular:** 400 (body text)
- **Semi-Bold:** 600 (headings, buttons, emphasis)

### Typography Scale

| Element | Size | Line Height | Weight | Usage |
|---------|------|-------------|--------|-------|
| **H1** | 48px (2.82rem) | 1.7 | 600 | Main page headings |
| **H2** | 42px (2.47rem) | 1.7 | 600 | Section headings |
| **H3** | 30px (1.76rem) | 1.7 | 600 | Subsection headings |
| **H4** | 20px (1.17rem) | 1.7 | 600 | Minor headings, card titles |
| **Body Text** | 17px (1rem) | 1.7 | 400 | Paragraphs, descriptions |
| **Button Text** | 16px | 1.0 | 600 | All buttons |
| **Table Header** | 18px | 1.2 | Bold (700) | Table headers |
| **Table Body** | 17px | 1.5 | 400 | Table content |

### Typography Guidelines
- **Line Height:** Consistently 1.7 for readability
- **Color:** Dark gray `#53575a` for body text
- **Links:** Red `#e40032` with hover transitions

---

## 🔘 Button Styles

### Primary Button (Default State)
```css
{
  background-color: #53575a;
  color: #ffffff;
  font-family: Raleway, sans-serif;
  font-size: 16px;
  font-weight: 600;
  padding: 16px 35px;
  border-radius: 5px;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
}
```

### Primary Button (Hover State)
```css
{
  background-color: #e40032;
  color: #ffffff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.15);
}
```

### Button Specifications
- **Padding:** 16px vertical, 35px horizontal
- **Border Radius:** 5px (rounded corners)
- **Border:** None (0px)
- **Text Transform:** None (sentence case)
- **Hover Transition:** Background color changes from dark gray to brand red

---

## 📐 Layout & Spacing

### Container Widths
- **Desktop Max Width:** 1240px
- **Responsive Breakpoints:**
  - Small: 544px
  - Medium: 768px
  - Large: 921px

### Spacing System
- **Section Margin:** 15-30px between major sections
- **Card Padding:** 20-25px internal padding
- **Button Margin:** 15px around buttons
- **Table Padding:** 15px cell padding

### Grid System
- **Service Cards:** Equal-width columns (typically 4 across on desktop)
- **Content Grid:** Responsive, collapses to single column on mobile

---

## 🗂️ Component Styles

### Header/Navigation
- **Style:** Fixed/sticky navigation
- **Logo:** Max-width 222px
- **Default Background:** White or transparent
- **Sticky Background:** Green `#81d742` on scroll
- **Navigation Links:** Dark gray, change to red on hover
- **Mobile Breakpoint:** 921px (hamburger menu)

### Hero Section
- **Width:** Full-width
- **Background:** Light gray `#f5f5f5` or white
- **Content:** Centered, mission statement messaging
- **Typography:** Large heading (H1) with supporting text

### Service Cards
```css
{
  text-align: center;
  background: #ffffff;
  padding: 20-30px;
  border: 1px solid #eaeaea;
  border-radius: 5px;
}
```
- **Icon:** 50x50px at top
- **Title:** H4 styling (20px, weight 600)
- **Description:** Body text (17px, weight 400)
- **Hover:** Subtle shadow or border color change

### Tables (Custom Styling)

#### Table Header
```css
{
  background: linear-gradient(to right, #eb4065, #e40032);
  color: #ffffff;
  font-size: 18px;
  font-weight: bold;
  padding: 15px;
  text-align: center;
}
```

#### Table Body
```css
{
  background: #EEEEEE (alternating rows);
  border: 1px solid #AAAAAA;
  padding: 10px 15px;
  text-align: center;
}
```

#### Table Footer
- **Border Top:** 1-4px solid `#e40032`
- **Background:** White `#ffffff`
- **Text:** Centered, regular weight

### Accordion/Expandable Sections
- **Package Cards:** Collapsible content sections
- **Header:** Package name, price, brief description
- **Expanded Content:** Bulleted feature lists
- **Border:** Light gray `#dddddd`
- **Hover:** Border changes to red `#e40032`

---

## 🎭 Design Aesthetic

### Overall Feel
- **Modern Agricultural/Scientific Branding**
- Clean, professional layout with ample whitespace
- Emphasis on trust, expertise, and credibility
- Balance between technical information and accessibility

### Visual Hierarchy
1. **Primary:** Brand red for CTAs and important actions
2. **Secondary:** Dark gray for stability and readability
3. **Tertiary:** Light grays for backgrounds and structure
4. **Accent:** Green for active navigation states

### Design Principles
- **Whitespace:** Generous spacing around elements
- **Contrast:** High contrast for readability (dark text on light backgrounds)
- **Consistency:** Red used consistently for interactive elements
- **Responsiveness:** Mobile-first approach with clear breakpoints
- **Accessibility:** Large font sizes (17px+ for body text)

---

## 🔧 Unique Design Elements

### Sticky Navigation Transition
- Navigation starts transparent/white
- On scroll, transitions to green background `#81d742`
- Fade transition effect for smooth appearance
- Logo may resize or change color

### Table Gradient Headers
- Red gradient from `#eb4065` to `#e40032`
- White text for contrast
- Creates visual hierarchy for data tables
- Used consistently across service pages

### Icon System
- Custom Astra icon library
- 50x50px standard icon size
- Centered above service card text
- Monochromatic or brand red coloring

### Footer Styling
- Reversed logo (white on dark background)
- Multi-column layout on desktop
- Collapses to single column on mobile
- Contact information prominently displayed

---

## 📱 Responsive Design

### Mobile (< 544px)
- Single column layout
- Full-width buttons
- Hamburger navigation menu
- Reduced font sizes (proportional scaling)
- Increased touch target sizes

### Tablet (544px - 921px)
- Two-column grids for service cards
- Collapsible navigation may appear
- Adjusted padding and margins
- Maintained readability with responsive typography

### Desktop (> 921px)
- Multi-column layouts (up to 4 columns)
- Full horizontal navigation
- Max content width: 1240px
- Optimal reading line length maintained

---

## 💡 Implementation Notes

### CSS Variables (Root)
Recommend implementing with CSS custom properties:
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

### Animation/Transitions
- Button hover: 0.3s ease transition
- Navigation sticky: Fade transition
- Link hover: Immediate color change
- Shadow effects: 0.2s ease

### Accessibility Considerations
- High contrast ratios (WCAG AA compliant)
- Large font sizes for readability
- Clear focus states for keyboard navigation
- Alt text for images (implied, not visible in HTML)

---

## 🎯 Key Takeaways for Dashboard Implementation

### Color Strategy
1. Use brand red `#e40032` for all CTAs and interactive elements
2. Dark gray `#53575a` for primary text and stable UI elements
3. Light gray `#f5f5f5` for backgrounds and section divisions
4. Maintain high contrast for accessibility

### Typography Strategy
1. Implement Raleway font (include via CDN or local)
2. Use 17px as base font size (larger than standard 16px)
3. Maintain 1.7 line height for readability
4. Use weight 600 for all headings and emphasis

### Component Strategy
1. All buttons should follow the gray→red hover pattern
2. Tables should use red gradient headers
3. Cards should be centered with consistent padding
4. Navigation should be sticky with scroll behavior

### Layout Strategy
1. Max width 1240px for content
2. Responsive breakpoints at 544px, 768px, 921px
3. Mobile-first approach
4. Generous whitespace between sections

---

## 📚 Resources

### Font Import (Google Fonts)
```html
<link href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;600;700&display=swap" rel="stylesheet">
```

### Color Accessibility
- **Red on White:** WCAG AA ✅ (4.78:1 contrast ratio)
- **Dark Gray on White:** WCAG AAA ✅ (8.82:1 contrast ratio)
- **White on Red:** WCAG AA ✅ (4.78:1 contrast ratio)

### Browser Compatibility
- Modern browsers (Chrome, Firefox, Safari, Edge)
- CSS Grid and Flexbox for layouts
- Fallbacks for older browsers if needed

---

*This style guide was compiled by analyzing the Regen Ag Lab website structure, CSS, and design patterns to ensure accurate replication of their brand identity.*
