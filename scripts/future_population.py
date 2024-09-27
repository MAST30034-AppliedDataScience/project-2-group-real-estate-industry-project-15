# Import libraries
import os
import io
import requests
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# URL to the excel file containing future population data 
url = "https://www.planning.vic.gov.au/__data/assets/excel_doc/0028/691660/VIF2023_SA2_Pop_Hhold_Dwelling_Projections_to_2036_Release_2.xlsx"
response = requests.get(url)

df = pd.read_excel(io.BytesIO(response.content), sheet_name='Total_Population', skiprows=9)

# Save the data into a CSV file in the specified directory
df.to_csv("../data/landing/future_population.csv", index=False)