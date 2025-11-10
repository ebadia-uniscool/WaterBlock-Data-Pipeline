import pandas as pd


# File paths
csv_file_1 = 'AD_102_100.csv'  # Path to the first CSV file
csv_file_2 = 'TL_102_100.CSV'  # Path to the second CSV file
merged_output_file = '102RPM100.csv'  # Path to save the merged output

# ------------------------------ DOCUMENT JOINER ----------------------------- #

def merge_csv_files(csv_file_1, csv_file_2, output_file_csv):
    """
    Merge two CSV files side by side and save to a new file.
    """
    # Read the CSV files into pandas DataFrames
    df1 = pd.read_csv(csv_file_1)
    df2 = pd.read_csv(csv_file_2)

    # Merge the two DataFrames along columns (side by side)
    merged_df = pd.concat([df1, df2], axis=1)

    # Save the merged DataFrame to a new CSV file
    merged_df.to_csv(output_file_csv, index=False)


    print(f"Merged file saved as {output_file_csv}")

# -------------------------------- MAIN RUNNER ------------------------------- #

# Merge the CSV files
merge_csv_files(csv_file_1, csv_file_2, merged_output_file)
