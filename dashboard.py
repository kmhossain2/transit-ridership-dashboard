import pandas as pd

# Load the Excel file, skipping the first 5 rows of title/info
data = pd.read_excel("TTC_Ridership_Data.xlsx", engine="openpyxl", skiprows=5)

# Drop empty columns
data = data.dropna(axis=1, how='all')

# Drop empty rows
data = data.dropna(axis=0, how='all')

# Show first few rows
print("Cleaned data:")
print(data.head())

# Show column names
print("\nColumns:")
print(data.columns)


import matplotlib.pyplot as plt

# Step 1: Remove the first column (it's just labels like WHO/WHAT)
data_cleaned = data.drop(columns=['Unnamed: 0'])

# Step 2: Set "FARE MEDIA" as the row label (index)
data_cleaned = data_cleaned.set_index('  FARE MEDIA')

# Step 3: Transpose the table so years are rows and fare types are columns
transposed = data_cleaned.transpose()

# Step 4: Convert all values to numeric (just in case)
transposed = transposed.apply(pd.to_numeric, errors='coerce')

# Step 5: Sum across all fare types to get total per year
total_riders_per_year = transposed.sum(axis=1)

# Step 6: Plot
plt.figure(figsize=(12, 6))
plt.bar(total_riders_per_year.index.astype(str), total_riders_per_year.values)
plt.xticks(rotation=45)
plt.title("Total TTC Ridership Per Year (1985–2019)")
plt.xlabel("Year")
plt.ylabel("Total Riders (in thousands)")
plt.tight_layout()
plt.grid(axis='y')
plt.show()
