# 📊 Vendor Performance Analysis

### End-to-End Data Analytics Project using SQL, Python & Power BI

An end-to-end **Vendor Performance Analysis** project designed to evaluate vendor profitability, purchasing efficiency, inventory turnover, sales performance, and supplier dependency for a retail and wholesale business.

The project demonstrates a complete analytics workflow — from **raw CSV data ingestion and SQL-based transformation to Python exploratory analysis, statistical testing, Power BI visualization, and business recommendations**.

---

## 📌 Table of Contents

- [Business Problem](#-business-problem)
- [Objectives](#-objectives)
- [Project Workflow](#-project-workflow)
- [Dataset](#-dataset)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [SQL Analysis](#-sql-analysis)
- [Python Analysis](#-python-analysis)
- [Statistical Analysis](#-statistical-analysis)
- [Power BI Dashboard](#-power-bi-dashboard)
- [Key Insights](#-key-insights)
- [Business Recommendations](#-business-recommendations)
- [How to Run](#-how-to-run)
- [Skills Demonstrated](#-skills-demonstrated)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

# 🎯 Business Problem

Retail and wholesale businesses work with multiple vendors and thousands of products.

Poor vendor management can result in:

- Low profit margins
- High purchasing costs
- Excess inventory
- Slow-moving products
- High inventory holding costs
- Vendor dependency
- Inefficient bulk purchasing
- Supply-chain risks

The purpose of this project is to analyze vendor and product-level data and identify opportunities to **increase profitability, improve inventory efficiency, and optimize vendor relationships**.

---

# 🎯 Objectives

The primary objectives of this analysis are:

- Identify high-performing and underperforming vendors.
- Analyze vendor contribution to total purchases and sales.
- Identify vendors generating the highest gross profit.
- Analyze vendor profitability and profit margins.
- Evaluate the relationship between purchase quantity and unit cost.
- Determine whether bulk purchasing provides cost advantages.
- Analyze inventory turnover.
- Identify slow-moving and inefficient inventory.
- Measure vendor concentration and dependency.
- Statistically compare high-performing and low-performing vendors.
- Provide actionable recommendations for management.

---

# 🔄 Project Workflow

```text
                 BUSINESS PROBLEM
                        │
                        ▼
                 RAW CSV DATA
                        │
                        ▼
              DATA INGESTION / ETL
                        │
                        ▼
                SQLite DATABASE
                        │
                        ▼
             SQL DATA EXPLORATION
                        │
                        ▼
              DATA CLEANING & JOINING
                        │
                        ▼
             VENDOR SUMMARY TABLE
                        │
                        ▼
              PYTHON EDA & ANALYSIS
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
        Visualization       Statistical Testing
              │                   │
              └─────────┬─────────┘
                        ▼
                POWER BI DASHBOARD
                        │
                        ▼
              BUSINESS INSIGHTS
                        │
                        ▼
             RECOMMENDATIONS REPORT
```

---

# 🗂️ Dataset

The project uses six major source files.

| File | Description |
|---|---|
| `begin_inventory.csv` | Inventory available at the beginning of the analysis period |
| `end_inventory.csv` | Inventory available at the end of the analysis period |
| `purchase_prices.csv` | Product-level purchase price information |
| `purchases.csv` | Vendor purchase transactions |
| `sales.csv` | Sales transaction data |
| `vendor_invoice.csv` | Vendor invoice and freight information |

### ⚠️ Large Dataset

The `sales.csv` file is approximately **1.5 GB** and may not be included in the GitHub repository because of GitHub file-size limitations.

To run the complete project locally, place the dataset inside:

```text
data/sales.csv
```

---

# 🛠️ Tech Stack

### Programming & Analytics

- Python
- Pandas
- NumPy
- SciPy

### Data Visualization

- Matplotlib
- Seaborn
- Power BI

### Database

- SQLite
- SQL
- SQLAlchemy

### Development Environment

- Jupyter Notebook
- VS Code

### Reporting

- Power BI Dashboard
- Business Analysis Report

---

# 📁 Project Structure

```text
vendor-performance-analysis/
│
├── data/
│   ├── begin_inventory.csv
│   ├── end_inventory.csv
│   ├── purchase_prices.csv
│   ├── purchases.csv
│   ├── sales.csv
│   └── vendor_invoice.csv
│
├── database/
│   └── vendor_analysis.db
│
├── sql/
│   ├── 01_data_exploration.sql
│   ├── 02_data_cleaning.sql
│   ├── 03_data_transformation.sql
│   ├── 04_vendor_analysis.sql
│   └── 05_vendor_summary.sql
│
├── scripts/
│   ├── data_ingestion.py
│   ├── data_validation.py
│   └── etl_pipeline.py
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_vendor_analysis.ipynb
│   └── 03_hypothesis_testing.ipynb
│
├── dashboard/
│   └── Vendor_Performance.pbix
│
├── reports/
│   └── Vendor_Performance_Report.pdf
│
├── images/
│   ├── dashboard.png
│   ├── vendor_analysis.png
│   └── inventory_analysis.png
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🧹 Data Ingestion & ETL

The project follows a structured ETL process.

### Extract

Raw CSV files are collected from different business operations:

```text
Inventory
Purchases
Sales
Vendor Invoices
Purchase Prices
```

### Transform

The data is:

- Loaded into Python/SQLite.
- Validated for missing values.
- Checked for duplicate records.
- Converted into appropriate data types.
- Joined using relevant keys.
- Aggregated at the vendor and product levels.
- Prepared for analytical reporting.

### Load

The transformed datasets are stored in a SQLite database and used for downstream SQL, Python, and Power BI analysis.

---

# 🗄️ SQL Analysis

SQL is used as the primary data transformation and aggregation layer.

### Major SQL Tasks

- Explore database tables.
- Check row counts and data types.
- Identify missing values.
- Identify duplicate records.
- Analyze vendor contribution.
- Join purchase and sales information.
- Combine inventory and pricing information.
- Calculate vendor-level metrics.
- Calculate product-level metrics.
- Build an aggregated vendor summary table.

### Example Business Metrics

```text
Total Sales
Total Purchases
Total Profit
Gross Profit Margin
Purchase Contribution %
Average Unit Cost
Inventory Turnover
Vendor Sales Contribution
Vendor Profit Contribution
```

---

# 🐍 Python Exploratory Data Analysis

Python is used to perform deeper exploratory analysis after the SQL transformation stage.

### Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
```

### EDA Includes

- Descriptive statistics
- Distribution analysis
- Missing-value analysis
- Outlier detection
- Vendor comparison
- Product analysis
- Profitability analysis
- Correlation analysis
- Inventory analysis
- Purchase-price analysis

---

# 📊 Key Analytical Questions

The analysis attempts to answer the following questions:

### Vendor Performance

1. Which vendors generate the highest sales?
2. Which vendors generate the highest gross profit?
3. Which vendors have the highest profit margins?
4. Which vendors are underperforming?

### Purchasing

5. Does purchasing larger quantities reduce unit cost?
6. Which vendors provide the best purchasing prices?
7. How much does freight cost affect profitability?

### Inventory

8. Which products have low inventory turnover?
9. Which vendors are associated with slow-moving inventory?
10. Where can inventory holding costs be reduced?

### Vendor Dependency

11. What percentage of purchases comes from the top vendors?
12. Is the business overly dependent on a small number of suppliers?

### Profitability

13. Are high-sales vendors also high-profit vendors?
14. What factors contribute most to vendor profitability?

---

# 🧪 Statistical Analysis

Statistical testing is used to validate whether observed differences in vendor performance are statistically meaningful.

## Hypothesis Testing

One of the major research questions is:

> **Is there a statistically significant difference in profit margins between high-performing and low-performing vendors?**

### Null Hypothesis

```text
H₀:
There is no significant difference in profit margins
between high-performing and low-performing vendors.
```

### Alternative Hypothesis

```text
H₁:
There is a significant difference in profit margins
between high-performing and low-performing vendors.
```

A statistical test such as an independent-samples **t-test** is used to evaluate the hypothesis.

---

# 📐 Confidence Intervals

Confidence intervals are calculated to estimate the range within which the true population metric is likely to fall.

This helps avoid making business decisions based only on point estimates.

---

# 📈 Power BI Dashboard

The Power BI dashboard provides an interactive view of vendor and business performance.

### Executive KPIs

- 💰 Total Sales
- 🛒 Total Purchases
- 📈 Gross Profit
- 📊 Gross Profit Margin
- 🏢 Total Vendors
- 📦 Total Products
- 💼 Inventory Value
- 🔄 Inventory Turnover

### Vendor Analysis

The dashboard allows users to analyze:

- Vendor sales
- Vendor contribution
- Vendor profitability
- Vendor ranking
- Purchase contribution
- Average unit cost
- Profit margin

### Inventory Analysis

The dashboard covers:

- Beginning inventory
- Ending inventory
- Inventory turnover
- Slow-moving inventory
- Inventory value
- Product-level performance

### Purchasing Analysis

The dashboard helps identify:

- Purchase volume
- Purchase cost
- Average unit price
- Bulk purchasing opportunities
- Vendor pricing differences

---

# 🔍 Key Insights

The analysis identified significant vendor concentration.

### Vendor Concentration

The **top 10 vendors account for approximately 65.69% of total purchase contribution**, while the remaining vendors contribute approximately 34.31%.

This indicates a relatively high dependency on a small group of suppliers.

### Leading Vendors

The major vendors by purchase contribution include:

| Vendor | Approx. Contribution |
|---|---:|
| Diageo North America | 16.3% |
| Martignetti Companies | 8.3% |
| Pernod Ricard USA | 7.8% |
| Jim Beam Brands | 7.6% |

These vendors represent a significant portion of the company's purchasing activity.

> **Note:** Additional findings such as bulk purchasing savings, slow-moving inventory, low-margin products, and vendor profitability should be updated after completing the final analysis.

---

# 💡 Business Recommendations

Based on the analysis, the following strategies can help improve business performance.

### 1. Diversify Vendor Base

The company should reduce excessive dependency on a small number of vendors.

Possible actions:

- Develop alternative suppliers.
- Maintain backup vendors.
- Negotiate with multiple suppliers.
- Monitor vendor concentration regularly.

---

### 2. Improve Underperforming Brands

Low-margin or underperforming products should be reviewed.

Possible actions:

- Adjust pricing.
- Introduce promotional campaigns.
- Negotiate better purchase prices.
- Reduce procurement of consistently poor-performing products.

---

### 3. Optimize Bulk Purchasing

Bulk purchasing should be used strategically.

Large orders may reduce unit costs, but excessive purchasing can increase:

- Inventory holding costs
- Storage requirements
- Working capital requirements
- Risk of obsolete inventory

Therefore, bulk purchasing should be evaluated together with inventory turnover.

---

### 4. Improve Inventory Turnover

Slow-moving inventory should be identified and managed.

Possible actions:

- Promotions
- Discounts
- Better demand forecasting
- Reduced purchase quantities
- Vendor return negotiations

---

### 5. Monitor Vendor Profitability

Management should evaluate vendors using multiple KPIs instead of sales alone.

A vendor with high sales but low margins may be less valuable than a vendor generating moderate sales with significantly higher profitability.

---

# 📌 Skills Demonstrated

This project demonstrates practical experience in:

### Data Analytics

- Data Cleaning
- Exploratory Data Analysis
- Statistical Analysis
- Business Analysis
- KPI Development

### SQL

- SELECT queries
- Filtering
- Aggregations
- GROUP BY
- JOINs
- Subqueries
- CTEs
- Data transformation

### Python

- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- Jupyter Notebook

### Database

- SQLite
- Relational Data Modeling
- SQLAlchemy
- ETL

### Business Intelligence

- Power BI
- Data Modeling
- DAX
- Interactive Dashboards
- KPI Visualization

### Professional Practices

- Modular project structure
- Logging
- Data validation
- Statistical validation
- Business recommendations
- Documentation

---

# 🚀 How to Run

## 1. Clone the Repository

```bash
git clone https://github.com/adityadahiya12/vendor-performance-analysis.git
```

Navigate to the project:

```bash
cd vendor-performance-analysis
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install pandas numpy matplotlib seaborn scipy sqlalchemy jupyter
```

---

## 4. Add Dataset

Place the CSV files inside:

```text
data/
```

Make sure the directory contains:

```text
data/
├── begin_inventory.csv
├── end_inventory.csv
├── purchase_prices.csv
├── purchases.csv
├── sales.csv
└── vendor_invoice.csv
```

---

## 5. Run the ETL Pipeline

```bash
python scripts/etl_pipeline.py
```

The pipeline prepares the data for analysis and stores the processed information in the database.

---

## 6. Run SQL Analysis

Execute the SQL scripts in the following order:

```text
01_data_exploration.sql
02_data_cleaning.sql
03_data_transformation.sql
04_vendor_analysis.sql
05_vendor_summary.sql
```

---

## 7. Launch Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
notebooks/01_EDA.ipynb
```

Then continue with the vendor analysis and hypothesis-testing notebooks.

---

## 8. Open Power BI Dashboard

Open:

```text
dashboard/Vendor_Performance.pbix
```

in **Power BI Desktop**.

Update the data source path if required.

---

# 📊 Expected Project Outcome

At the end of this project, the business receives:

```text
Raw Business Data
        ↓
Clean Structured Database
        ↓
Vendor-Level Analytics
        ↓
Statistical Validation
        ↓
Interactive Power BI Dashboard
        ↓
Business Insights
        ↓
Actionable Recommendations
```

The final solution helps management make data-driven decisions regarding:

- Vendor selection
- Purchasing strategy
- Inventory management
- Product pricing
- Supplier diversification
- Profitability improvement

---

# 🔮 Future Improvements

Potential improvements include:

- Automating the complete ETL pipeline.
- Connecting Power BI directly to the database.
- Adding automated data-quality checks.
- Implementing scheduled dashboard refreshes.
- Building vendor risk scores.
- Adding sales forecasting.
- Developing inventory demand forecasting.
- Implementing machine-learning-based vendor classification.
- Creating automated business alerts for low-margin vendors.
- Deploying the analytics pipeline to the cloud.

---

# 👨‍💻 Author

**Aditya Dahiya**

Full Stack Developer | Data Analytics Enthusiast

### Skills

`SQL` • `Python` • `Pandas` • `Power BI` • `Excel` • `JavaScript` • `React` • `Node.js` • `MongoDB`

---

## ⭐ Project

If you found this project useful, consider giving the repository a ⭐.

---

## 📚 Credits

This project was developed as an end-to-end vendor performance analytics case study inspired by the **Vendor Performance Data Analytics** project walkthrough by **Tech Classes**.

The implementation, analysis, visualizations, and business recommendations can be further customized based on the actual dataset and analytical findings.
