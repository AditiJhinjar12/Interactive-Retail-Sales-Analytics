# InsightView: Interactive Retail Sales Analytics Dashboard

An interactive dashboard that turns retail transaction data into clear, decision-ready insights on sales, profit, and customer behavior.

**[Live Demo]([link])** | **[Dashboard Screenshot](#preview)**

## Problem Statement
A retail store needs to know which products, regions, and customer segments drive profit, and where it is losing money despite strong sales. This dashboard answers those questions in one place.

## Dataset
- **Source:** [Superstore Dataset (Kaggle)](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- **Size:** [X] orders, [Y] columns, [start year] to [end year]
- **Key fields:** Order Date, Segment, Region, State, Category, Sub-Category, Sales, Quantity, Discount, Profit

## Tools Used
[Power BI / Tableau / HTML + JavaScript] | [SQL] | Python (pandas) | Excel

## Approach
1. **Data cleaning:** [handled missing values, removed duplicates, fixed date formats and data types]
2. **Analysis:** [SQL / pandas aggregations by category, region, segment, and month]
3. **Dashboard design:** built KPI cards, trend and comparison charts, and interactive filters
4. **Insights:** validated key figures against the raw data before summarizing findings

## Dashboard Features
- **KPI cards:** Total Sales, Profit, Profit Margin %, Orders, Average Order Value, YoY Growth
- **Trends:** monthly and yearly sales and profit
- **Breakdowns:** by category, sub-category, region, and customer segment
- **Top products:** best sellers vs most profitable
- **Discount analysis:** how discount levels affect profit
- **Filters:** date range, region, category, segment

## Key Insights
1. [e.g., Category X generates Y% of sales but only Z% of profit]
2. [e.g., Discounts above X% lead to negative profit]
3. [e.g., Sales peak in Nov to Dec each year]
4. [e.g., Region X is the top performer while Region Y lags]

## Preview
![Dashboard Screenshot](images/dashboard.png)

## How to Run
```bash
git clone https://github.com/[your-username]/[repo-name].git
cd [repo-name]
# Power BI/Tableau: open the .pbix/.twbx file
# HTML version: open index.html and load the dataset CSV
```

## Project Structure
```
├── data/          # dataset (or link to source)
├── sql/           # cleaning and analysis queries
├── notebooks/     # Python exploration
├── dashboard/     # .pbix / .twbx / index.html
├── images/        # screenshots
└── README.md
```

## What I Learned
[e.g., cleaning real-world data, writing DAX/SQL aggregations, turning numbers into business recommendations]

## Author
**Aditi Jhinjar** | [LinkedIn](https://linkedin.com/in/aditi-jhinjar-63040a28b) | [GitHub](https://github.com/AditiJhinjar12)
