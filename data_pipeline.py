import pandas as pd
from sqlalchemy import create_engine

# Database connection (replace with your actual credentials)
DATABASE_URL = "postgresql+psycopg2://YOUR_USERNAME:YOUR_PASSWORD@YOUR_HOST/neondb?sslmode=require"

# Path to CSV file (replace with your actual file path)
file_path = r"path/to/your/Amazon_Sale_Report.csv"

print("Reading data...")
df = pd.read_csv(file_path, low_memory=False)

print("Cleaning data and handling missing values...")

if 'Amount' in df.columns:
    df['Amount'] = df['Amount'].fillna(0)

if 'Qty' in df.columns:
    df['Qty'] = df['Qty'].fillna(0)

df = df.fillna('Unknown')

engine = create_engine(DATABASE_URL)

print("Uploading cleaned data to Neon...")
df.to_sql('supply_chain_inventory', con=engine, if_exists='replace', index=False)

print("Cleaned data successfully uploaded to database!")

print("\nQuick statistical summary from database:")
stats_query = """
SELECT 
    COUNT(*) AS total_rows,
    SUM("Amount") AS total_sales,
    COUNT(DISTINCT "Order ID") AS total_orders
FROM supply_chain_inventory;
"""
stats_df = pd.read_sql(stats_query, con=engine)
print(stats_df)