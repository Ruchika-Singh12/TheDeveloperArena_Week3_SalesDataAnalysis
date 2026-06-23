# ============================================================
# Week 3 Project: Sales Data Analysis
# Topic: Introduction to Data Analysis - Working with Real Data
# ============================================================

import pandas as pd

# -------------------------------------------------------
# STEP 1: Load the Dataset
# -------------------------------------------------------
print("=" * 55)
print("       SALES DATA ANALYSIS - WEEK 3 PROJECT")
print("=" * 55)

df = pd.read_csv('sales_data.csv')
print("\n✅ Dataset loaded successfully!")

# -------------------------------------------------------
# STEP 2: Explore the Data
# -------------------------------------------------------
print("\n📋 STEP 2: Exploring the Data")
print("-" * 40)
print(f"Total Rows    : {df.shape[0]}")
print(f"Total Columns : {df.shape[1]}")
print(f"\nColumn Names  : {list(df.columns)}")
print("\nData Types:")
print(df.dtypes)
print("\nFirst 5 Rows of Dataset:")
print(df.head())

# -------------------------------------------------------
# STEP 3: Handle Missing Values (Data Cleaning)
# -------------------------------------------------------
print("\n🧹 STEP 3: Checking for Missing Values")
print("-" * 40)
missing = df.isnull().sum()
print(missing)

if missing.sum() == 0:
    print("\n✅ No missing values found! Data is clean.")
else:
    print("\n⚠️  Filling missing numeric values with column mean...")
    df.fillna(df.select_dtypes(include='number').mean(), inplace=True)
    print("✅ Missing values handled.")

# -------------------------------------------------------
# STEP 4: Basic Statistics
# -------------------------------------------------------
print("\n📊 STEP 4: Basic Statistics")
print("-" * 40)
print(df.describe())

# -------------------------------------------------------
# STEP 5: Sales Analysis - 5 Different Metrics
# -------------------------------------------------------
print("\n🔍 STEP 5: Sales Analysis")
print("=" * 55)

# Metric 1: Total Revenue
total_revenue = df['Total_Sales'].sum()
print(f"\n💰 Metric 1 - Total Revenue:")
print(f"   ₹{total_revenue:,.2f}")

# Metric 2: Best Selling Product (by revenue)
product_revenue = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)
best_product = product_revenue.idxmax()
print(f"\n🏆 Metric 2 - Best Selling Product (by Revenue):")
print(f"   {best_product} → ₹{product_revenue[best_product]:,.2f}")
print("\n   All Products Revenue:")
for product, revenue in product_revenue.items():
    print(f"   {product:<15} ₹{revenue:>12,.2f}")

# Metric 3: Best Region
region_sales = df.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False)
best_region = region_sales.idxmax()
print(f"\n🌍 Metric 3 - Best Performing Region:")
print(f"   {best_region} → ₹{region_sales[best_region]:,.2f}")
print("\n   All Regions Sales:")
for region, sales in region_sales.items():
    print(f"   {region:<10} ₹{sales:>12,.2f}")

# Metric 4: Average Order Value
avg_order = df['Total_Sales'].mean()
max_sale   = df['Total_Sales'].max()
min_sale   = df['Total_Sales'].min()
print(f"\n📈 Metric 4 - Order Value Statistics:")
print(f"   Average Order Value : ₹{avg_order:,.2f}")
print(f"   Highest Single Sale : ₹{max_sale:,.2f}")
print(f"   Lowest Single Sale  : ₹{min_sale:,.2f}")

# Metric 5: Product sold by quantity
product_qty = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
print(f"\n📦 Metric 5 - Products Sold by Quantity:")
for product, qty in product_qty.items():
    print(f"   {product:<15} {qty} units")

# -------------------------------------------------------
# STEP 6: Final Summary Report
# -------------------------------------------------------
print("\n" + "=" * 55)
print("           📝 FINAL ANALYSIS REPORT")
print("=" * 55)
print(f"  Total Transactions  : {len(df)}")
print(f"  Total Revenue       : ₹{total_revenue:,.2f}")
print(f"  Best Product        : {best_product}")
print(f"  Best Region         : {best_region}")
print(f"  Avg Order Value     : ₹{avg_order:,.2f}")
print(f"  Highest Sale        : ₹{max_sale:,.2f}")
print(f"  Lowest Sale         : ₹{min_sale:,.2f}")
print("=" * 55)
print("\n✅ Analysis Complete!")
