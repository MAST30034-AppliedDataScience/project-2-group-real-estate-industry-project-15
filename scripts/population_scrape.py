# Import libraries
import os
import io
import requests
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# URL to the excel file containing population data 
url = "https://www.abs.gov.au/statistics/people/population/regional-population/2022-23/32180DS0001_2022-23.xlsx"
response = requests.get(url)

# Retrieve the data from the excel file (data starts in row 7 which is row 6 in python)
df = pd.read_excel(io.BytesIO(response.content), sheet_name='Table 2', skiprows=6)

# Hardcode the column headers due to difficulty in accurately retrieving these in the desired format
column_headers = [
    "GCCSA code", "GCCSA name", "SA4 code", "SA4 name", "SA3 code", "SA3 name", 
    "SA2 code", "SA2 name", "ERP at 30 June 2022 no.", "ERP at 30 June 2023 no.", 
    "ERP change 2022-23 no.", "ERP change 2022-23 %", 
    "Components of population change 2022-23 Natural increase no.", 
    "Components of population change 2022-23 Net internal migration no.", 
    "Components of population change 2022-23 Net overseas migration no.", 
    "Area (km2)", "Population density 2023 (persons/km2)"
]

df.columns = column_headers

# Save the data into a CSV file in the specified directory
df.to_csv("../data/landing/population.csv", index=False)

print(f"Victorian Population Data Successfully Downloaded!")