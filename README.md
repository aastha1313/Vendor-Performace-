📊 Vendor Performance Analysis Dashboard
This project aims to analyze vendor performance using Python (for data ingestion and exploratory data analysis) and Power BI (for dashboard visualization). The goal is to derive insights related to sales, profitability, inventory turnover, and vendor contribution.

🚀 Project Overview
We built an end-to-end data analytics pipeline:

✅ Ingested CSV files into a SQLite database

✅ Performed Exploratory Data Analysis (EDA) in Jupyter Notebook

✅ Visualized KPIs and insights using a Power BI dashboard

⚙️ Technologies Used
Python (pandas, numpy, matplotlib, seaborn)

SQLite (for lightweight database storage)

Power BI (for interactive data visualization)

Logging module (for tracking ingestion process)

SQLAlchemy (for Python-DB communication)

📦 Data Pipeline
🔹 Step 1: Ingest CSV to SQLite
python
Copy
Edit
from sqlalchemy import create_engine
import pandas as pd
import os

# Create SQLite engine
engine = create_engine('sqlite:///inventory.db')

# Ingest CSV files into the database
def ingest_db_chunked(file_path, table_name, engine, chunksize=100000):
    for chunk in pd.read_csv(file_path, chunksize=chunksize):
        chunk.to_sql(table_name, con=engine, if_exists='append', index=False)
🔹 Step 2: Load & Clean Data
EDA involved:

Removing entries with zero or negative sales/profits

Identifying outliers

Computing confidence intervals

Visualizing distribution of vendors and brands

📊 Key Business Insights
✅ 1. Sales & Profitability
Total Sales: $441.41M

Total Purchase: $307.34M

Gross Profit: $134.07M

Profit Margin: 38.72%

✅ 2. High-Margin, Low-Sales Brands
198 brands show high profit margins but low sales — strong candidates for promotional pricing.

✅ 3. Top Vendor Dependency
10 vendors contribute ~66% of total purchases — suggests over-reliance and risk in supply chain.

✅ 4. Bulk Purchase Advantage
Bulk buyers receive 72% cheaper per-unit prices → encourages inventory scaling for better margins.

✅ 5. Low Inventory Turnover
$2.71M worth of unsold inventory — opportunity to optimize procurement and storage.

✅ 6. Statistical Testing
Profit margins between high vs. low-performing vendors differ significantly (p < 0.05).

📈 Power BI Dashboard Highlights
KPIs: Sales, Profit, Unsold Capital, Margin%

Vendor Sales Breakdown

Inventory Turnover Chart

Target Brand Identification

Scatterplot of Profit Margin vs. Sales


✅ Recommendations
📉 Adjust pricing of low-sale, high-margin products

🔄 Diversify vendors to reduce risk

📦 Leverage bulk ordering for cost savings

🚚 Clear unsold inventory using discounting or promos

📢 Boost visibility for low-performing vendors through marketing

📌 How to Run
Place raw .csv files in data/ folder.

Run load_raw_data() from the script to ingest into inventory.db.

Use EDA_analysis.ipynb to explore insights.

Open dashboard.pbix in Power BI to view the live dashboard.
