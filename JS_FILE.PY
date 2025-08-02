import pandas as pd

# Load the data
df = pd.read_csv("Retail_sales_data.csv")

# Display top 5 rows
print(df.head())

# View column names, data types, and missing values
print(df.columns)
print(df.dtypes)
print(df.isnull().sum())
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
df.rename(columns={'quantity_solid': 'quantity_sold'}, inplace=True)
df['order_date'] = pd.to_datetime(df['order_date'])
df.dropna(inplace=True)   # Or: df.fillna(0, inplace=True)
print("Total_Sales:", df['total_sales'].sum())
print(df.groupby('product_name')['total_sales'].sum().sort_values(ascending=False))
df.set_index('order_date').resample('M')['total_sales'].sum().plot(title='Monthly Sales Trend')
print(df.groupby('total_sales')['total_sales'].sum().sort_values(ascending=False).head(10))
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("retail_sales_data.csv")
df.head()

# Clean column names
df.columns = df.columns.str.lower().str.replace(" ", "_")
# Convert order_date to datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# Check for nulls
print(df.isnull().sum())

# Drop duplicates
df.drop_duplicates(inplace=True)

# Add a new column for month-year
df["month_year"] = df["order_date"].dt.to_period("M")

# Reset index if needed
df.reset_index(drop=True, inplace=True)
print("Total Sales: ₹", df["total_sales"].sum())
print("Total Orders:", df["order_id"].nunique())
print("total_sale:", df["total_sales"].nunique())
monthly_sales = df.groupby("month_year")["total_sales"].sum()

monthly_sales.plot(kind="line", marker="o", figsize=(10,5), title="Monthly Sales Trend")
plt.ylabel("Total Sales (₹)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
top_products = df.groupby("product_name")["total_sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_products.values, y=top_products.index, palette="viridis")
plt.title("Top 10 Products by Total Sales")
plt.xlabel("Total Sales (₹)")
plt.ylabel("Product Name")
plt.tight_layout()
plt.show()
category_sales = df.groupby("category")["total_sales"].sum()

category_sales.plot(kind="pie", autopct='%1.1f%%', figsize=(6,6), title="Sales by Category")
plt.ylabel("")
plt.tight_layout()
plt.show()
salesperson_perf = df.groupby("salesperson")["total_sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,5))
sns.barplot(x=salesperson_perf.index, y=salesperson_perf.values)
plt.title("Sales by Salesperson")
plt.ylabel("Total Sales (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
df["unit_price"] = df["total_sales"] / df["unit_sold"]
df.to_csv("cleaned_retail_sales_data.csv", index=False)
