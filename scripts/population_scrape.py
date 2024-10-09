# Import libraries
import os
import io
import requests
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# URL to the excel file containing population data 
url = "https://www.abs.gov.au/statistics/people/population/regional-population/2022-23/32180DS0003_2001-23.xlsx"
response = requests.get(url)

# Retrieve the data from the excel file (data starts in row 7 which is row 6 in python)
df = pd.read_excel(io.BytesIO(response.content), sheet_name='Table 1', skiprows=5)

# Save the data into a CSV file in the specified directory
df.to_csv("../data/landing/new_population.csv", index=False)

print(f"Victorian Population Data Successfully Downloaded!")