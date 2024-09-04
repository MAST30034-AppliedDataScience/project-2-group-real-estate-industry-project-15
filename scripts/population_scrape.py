# # Downloading the population extrernal dataset using API

# from owslib.wfs import WebFeatureService
# import pandas as pd 
# import geopandas
# import folium
# import io
# import os

# script_dir = os.path.dirname(os.path.abspath(__file__))
# os.chdir(script_dir)

# WFS_USERNAME = 'kathleenfiona.wongso@student.unimelb.edu.au'
# WFS_PASSWORD= 'eyJzdWIiOiI4NmVjZTlmNy0wZTI5LTQzNzMtYmM1Zi03ZmU3N2ZjMDNjOTAiLCJjaGsiOiI3ODM1NGE1MyIsImV4cCI6MTczMjc2NDk0Nn0.YIt2Sca5iJvVbANz7NHFqDiCAFLoazwyvyLHqnSGnss'
# WFS_URL='https://adp.aurin.org.au/geoserver/wfs'

# api_client = WebFeatureService(url=WFS_URL,username=WFS_USERNAME, password=WFS_PASSWORD, version='1.1.0')

# response = api_client.getfeature(typename='datasource-AU_Govt_ABS-UoM_AURIN_DB_3:abs_regional_population_sa2_2001_2021', outputFormat='csv')

# out = open('../data/landing/population.csv', 'wb')
# out.write(response.read())
# out.close()

########################## UPDATED CODE ########################## 
# Import the Libraries 
import requests
import pandas as pd
import os
import io

# URL to the excel file contianing population data 
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

# Create the directory if it does not already exist
os.makedirs("../data/landing/", exist_ok=True)

# Save the data into a CSV file in the specified directory
df.to_csv("../data/landing/population.csv", index=False)

print(f"Victorian Population Data Successfully Downloaded!")