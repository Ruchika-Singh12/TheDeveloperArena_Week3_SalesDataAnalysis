# 📊 Sales Data Analysis Report
## Week 3 Project: Introduction to Data Analysis - Working with Real Data

---

## 🎯 Project Overview and Objectives

This project analyzes a real-world sales dataset using Python's **Pandas** library.

**Goals:**
- Load and explore a CSV sales dataset
- Handle missing/dirty data (data cleaning)
- Calculate at least 5 different sales metrics
- Identify the best-selling product and top-performing region
- Present findings in a clean, formatted report

---

## ⚙️ Setup and Installation Instructions

### Step 1: Install Python
Download Python from [python.org](https://python.org) and install it.

### Step 2: Install Required Library
```bash
pip install pandas
```

### Step 3: Place Files Together
Put these files in the same folder:
```
your-folder/
├── sales_analysis.py
├── sales_data.csv
├── analysis_report.md
└── requirements.txt
```

### Step 4: Run the Script
```bash
python sales_analysis.py
```

---

## 🗂️ Code Structure Explanation

| Section | What it Does |
|--------|--------------|
| **STEP 1** | Loads the CSV file into a Pandas DataFrame |
| **STEP 2** | Explores shape, columns, data types, first rows |
| **STEP 3** | Checks and handles missing values |
| **STEP 4** | Prints basic statistics (mean, min, max, etc.) |
| **STEP 5** | Calculates 5 different sales metrics |
| **STEP 6** | Prints a clean final summary report |

---

## 📋 Dataset Information

| Property | Value |
|----------|-------|
| File Name | sales_data.csv |
| Total Rows | 100 |
| Total Columns | 7 |
| Missing Values | None |

**Columns:**
- `Date` – Transaction date
- `Product` – Product name (Phone, Laptop, Tablet, Monitor, Headphones)
- `Quantity` – Units sold
- `Price` – Price per unit (₹)
- `Customer_ID` – Unique customer identifier
- `Region` – Sales region (North, South, East, West)
- `Total_Sales` – Total sale value = Quantity × Price

---

## 🔍 Analysis Findings

### 💰 Metric 1: Total Revenue
> **₹1,23,65,048.00**

Total revenue generated from all 100 transactions.

---

### 🏆 Metric 2: Best Selling Product (by Revenue)

| Product | Revenue (₹) |
|---------|-------------|
| 🥇 **Laptop** | **38,89,210** |
| Tablet | 28,84,340 |
| Phone | 28,59,394 |
| Headphones | 13,84,033 |
| Monitor | 13,48,071 |

**Winner: Laptop** – Highest revenue product.

---

### 🌍 Metric 3: Best Performing Region

| Region | Sales (₹) |
|--------|-----------|
| 🥇 **North** | **39,83,635** |
| South | 37,37,852 |
| East | 25,19,639 |
| West | 21,23,922 |

**Winner: North Region** – Top sales region.

---

### 📈 Metric 4: Order Value Statistics

| Statistic | Value (₹) |
|-----------|-----------|
| Average Order Value | 1,23,650.48 |
| Highest Single Sale | 3,73,932.00 |
| Lowest Single Sale | 6,540.00 |

---

### 📦 Metric 5: Products Sold by Quantity

| Product | Units Sold |
|---------|-----------|
| 🥇 Laptop | 136 units |
| Tablet | 127 units |
| Phone | 101 units |
| Monitor | 66 units |
| Headphones | 48 units |

---

## ✅ How Technical Requirements Were Met

| Requirement | How it was done |
|-------------|----------------|
| Use pandas to load and analyze data | `pd.read_csv()` and `.groupby()` used |
| Handle missing values | `df.isnull().sum()` checked; `fillna()` used if needed |
| Calculate at least 3 metrics | 5 metrics calculated (total revenue, best product, best region, avg order, qty sold) |
| Clean formatted report | Step 6 prints formatted report with borders |
| Add comments explaining each step | Every step has clear comments in the code |

---

## 💡 Key Insights

1. **Laptop** is the highest revenue-generating product (₹38.89 Lakh)
2. **North region** leads in sales performance (₹39.84 Lakh)
3. Average transaction value is around **₹1.24 Lakh**
4. Dataset is clean with **zero missing values**
5. Despite fewer units, Laptops outperform Tablets in revenue due to higher price

---

*Project completed for Week 3: Introduction to Data Analysis*
