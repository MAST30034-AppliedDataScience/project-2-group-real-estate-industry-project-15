import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Retrieve the data from the excel file (for all sheets)
rent_history_excel = "https://www.dffh.vic.gov.au/moving-annual-rent-suburb-march-quarter-2024-excel"

# Load all sheets into a dictionary of DataFrames
rent_history_df_dict = pd.read_excel(rent_history_excel, sheet_name=None, engine='openpyxl')

# Loop through each sheet and save to individual CSV files
for sheet_name, df in rent_history_df_dict.items():
    # Save each sheet to a separate CSV file
    df.to_csv(f'../data/landing/rent_history_{sheet_name}.csv', index=False)

print("Rental history data from all sheets has been downloaded!")
