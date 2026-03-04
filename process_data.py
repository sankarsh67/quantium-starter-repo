import pandas as pd

# Load the three CSV files
df0 = pd.read_csv("data/daily_sales_data_0.csv")
df1 = pd.read_csv("data/daily_sales_data_1.csv")
df2 = pd.read_csv("data/daily_sales_data_2.csv")

# Combine them
combined_df = pd.concat([df0, df1, df2], ignore_index=True)

# Filter only pink morsel (all lowercase)
pink_df = combined_df[combined_df["product"] == "pink morsel"].copy()

# Create Sales column
pink_df["Sales"] = pink_df["quantity"] * pink_df["price"]

# Keep only required columns
final_df = pink_df[["Sales", "date", "region"]]

# Rename columns properly
final_df.columns = ["Sales", "Date", "Region"]

# Save final output
final_df.to_csv("formatted_sales.csv", index=False)

print("Data processing complete. File saved as formatted_sales.csv")