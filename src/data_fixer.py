import pandas as pd

# Load the CSV file
input_csv = "102RPM100.csv"  # CSV file path
df = pd.read_csv(input_csv)

# Columns to process
columns_to_process = ['Water Temp IN', 'Water Temp OUT', 'Pump RPM']

# Process each column
for column in columns_to_process:
    # Ensure the column exists
    if column in df.columns:
        # Convert all values to numeric (forcing errors to NaN)
        df[column] = pd.to_numeric(df[column], errors='coerce')

        # Replace invalid entries, including 0s and < 10.
        df[column] = df[column].apply(
            lambda x: None if pd.isna(x) or x == 0 or x < 10 else x
        )
        
        # Fill missing values with the value from the previous row using ffill()
        df[column] = df[column].ffill()

    else:
        print(f"Warning: Column '{column}' not found in the CSV file.")

# Save the updated data to an Excel file
output_file = "F102RPM100.xlsx"
df.to_excel(output_file, index=False)
print(f"Updated file saved as {output_file}")
