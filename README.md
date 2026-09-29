# InsightView — Kaggle Superstore Sales & Profitability Dashboard

**InsightView** is a single self-contained HTML interactive retail sales dashboard designed for analyzing the Kaggle "Superstore" dataset (`vivek468/superstore-dataset-final`).

---

## 🚀 How to Run

1. Double-click **`index.html`** to open it directly in any browser (Chrome, Safari, Edge, Firefox), or
2. Run a simple local server if preferred:
   ```bash
   python3 -m http.server 8080
   ```
   Then navigate to `http://localhost:8080/index.html`.

---

## 📁 Files in this Folder

- **`index.html`**: The complete, self-contained dashboard application (includes HTML, CSS styling, Chart.js visualizations, Lucide icons, and the full data parsing & insights engine).
- **`superstore_sample.csv`**: A 1,200-row sample CSV formatted to match the exact schema of the Kaggle Superstore dataset.
- **`build_app.py`**: Python script used to assemble and update the dashboard.
- **`generate_full_sample.py`**: Script used to generate synthetic multi-year Superstore data.

---

## 📊 Dashboard Features

- **In-Browser CSV Parsing**: Supports drag-and-drop & file picker, handles UTF-8 / Latin-1 / Windows-1252 encodings, and maps columns automatically.
- **Pre-Loaded Demo Data**: Displays labeled sample data (`DEMO DATA - not real`) until a CSV is uploaded.
- **KPI Cards**: Total Sales, Total Profit, Profit Margin %, Total Orders, Average Order Value (AOV), and YoY Growth.
- **4 Automated Strategic Insights**:
  1. *Profit Leakage Alert* (identifies unprofitable sub-categories and root causes)
  2. *Discount Cliff Analysis* (shows margin decay across discount tiers)
  3. *Regional Performance* (ranks territory revenue & profit margins)
  4. *Segment & Seasonality Surge* (evaluates customer segment velocity and Q4 holiday peaks)
- **6 Interactive Visualizations**:
  - Monthly Revenue & Profit Dynamics (Time series with view toggles)
  - Sales & Profit by Category & Sub-Category
  - Sales & Profit by Region
  - Customer Segment Share & Margin %
  - Discount vs. Profitability Danger Curve
  - Top 10 Ranked Products (by Sales, Profit, or Loss)
- **Interactive Data Explorer**: Searchable, sortable, and paginated transaction table.
- **Theme Switcher**: Dark Mode and Light Mode with instant toggle.
