import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\m8cg2\OneDrive\Desktop\elevate lab data analyst intern\day-2 task\Superstore.csv", encoding='ISO-8859-1')

# Drop unnecessary columns
columns_to_keep = ['Order Date', 'Ship Date', 'Category', 'Sub-Category', 'Sales',
                   'Quantity', 'Profit', 'Discount', 'Region', 'Segment', 'State']
df = df[columns_to_keep]

# Convert dates to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')

# Drop rows with missing values
df.dropna(inplace=True)

# Optional: Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Save cleaned and reduced version
df.to_csv("cleaned_superstore.csv", index=False)
