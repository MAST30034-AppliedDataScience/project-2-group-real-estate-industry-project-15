import os
from urllib.request import urlretrieve
import pandas as pd

# Get our current working directory for the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Set the output diretory for the crime data cript
output_relative_dir = os.path.join(script_dir, '../data/')
crime_output_dir = os.path.join(output_relative_dir, 'landing')

os.makedirs(crime_output_dir, exist_ok=True)

#data set for crimes
dataset = "https://files.crimestatistics.vic.gov.au/2024-06/Data_Tables_LGA_Recorded_Offences_Year_Ending_December_2023_0.xlsx"


# Extract the filename from the URL
filename = os.path.basename(dataset)
# Construct the full output path
output_path = os.path.join(crime_output_dir, filename)
# Download and save the file
urlretrieve(dataset, output_path)
print(f"Downloaded {filename} to {output_path}")

#only save the relevent tab into a parquet
df_fifth_sheet = pd.read_excel(output_path, sheet_name="Table 03", header=0)

# Save the DataFrame to a Parquet file
output_parquet_path = os.path.join(crime_output_dir, "crime.parquet")
df_fifth_sheet.to_parquet(output_parquet_path)

print(f"Saved the fifth sheet (Table 03) to {output_parquet_path}")

