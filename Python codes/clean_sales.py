import pandas as pd

# Path to the input CSV file
input_csv_file = 'Updated_sales.csv'

# Path to the output CSV file
output_csv_file = 'cleaned_sales.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(input_csv_file)

# Drop rows where all elements are NaN
df_cleaned = df.dropna(how='all')

# Drop duplicate rows
df_cleaned = df_cleaned.drop_duplicates()

# Attempt to convert 'Order Date' to datetime format, handle errors
def parse_date(date_str):
    try:
        return pd.to_datetime(date_str, errors='coerce')
    except Exception as e:
        print(f"Error parsing date: {e}")
        return pd.NaT

df_cleaned['Order Date'] = df_cleaned['Order Date'].apply(parse_date)

# Drop rows where 'Order Date' could not be parsed
df_cleaned = df_cleaned.dropna(subset=['Order Date'])

# Create 'Order Time' column by extracting time from 'Order Date'
df_cleaned['Order Time'] = df_cleaned['Order Date'].dt.strftime('%I:%M:%S %p')

# Format 'Order Date' column to a specific date format (e.g., 'YYYY-MM-DD')
df_cleaned['Order Date'] = df_cleaned['Order Date'].dt.strftime('%Y-%m-%d')

# Optionally, reset the index after dropping rows
df_cleaned.reset_index(drop=True, inplace=True)

# Save the cleaned DataFrame back to a new CSV file
df_cleaned.to_csv(output_csv_file, index=False)

print(f"Empty rows and duplicates removed. 'Order Date' formatted to 'YYYY-MM-DD' and 'Order Time' extracted. Cleaned file saved to {output_csv_file}")
