# Import Libraries
import pandas as pd
import geopandas as gpd
import requests
import zipfile
import os
import pdfplumber
import re
import requests
import pandas as pd
from io import BytesIO
import pdfplumber
import pandas as pd
import re


################################# Shopping Centre Data #################################

# Retrieve the pdf file path 
shopping_centres_pdf = "../data/landing/Shopping Centres Data.pdf"

with pdfplumber.open(shopping_centres_pdf) as pdf:
    data = []

    # Iterate through each page
    for page_number, page in enumerate(pdf.pages, start=1):
        text = page.extract_text()

        if text: 
            # Store each new line in the text
            lines = text.split('\n')

            # Every 3 lines = one record
            for i in range(0, len(lines), 3):
                if i + 2 < len(lines):
                    centre_name = lines[i].strip()
                    centre_type = lines[i + 1].strip()
                    suburb = lines[i + 2].strip()
                    data.append([centre_name, centre_type, suburb])

        else:
            print(f"Warning: No text extracted on page {page_number}.")

# Create a dataframe from the data extracted
shopping_centres_df = pd.DataFrame(data, columns=["Centre name", "Centre Type", "Suburb"])

# Convert dataframe to csv file
shopping_centres_df.to_csv("../data/landing/shopping_centres.csv", index=False)

print("Data has been extracted and saved to shopping_centres.csv")




################################# Sports & Recreational Facilities  #################################

# Retrieve the data from the excel file and save it to a data frame
sports_facilities_excel = "https://discover.data.vic.gov.au/dataset/e6db797e-3801-4cfa-bf02-82350d0f722d/resource/bfff5fff-9c74-4671-8396-43f793613b70/download/srv_ifmd_all-facilities.xlsx"
sports_facilities_df = pd.read_excel(sports_facilities_excel, engine='openpyxl')

# Convert dataframe to csv file
sports_facilities_df.to_csv('../data/landing/sports_facilities.csv', index=False)

print("Sports & Recreational Facilities data has been downloaded!")




################################# Parks and Conservation Reserves #################################
# Shapefile has been uploaded




################################# Building Types #################################

# Download the .xlsb file from the URL
buildings_excel = "https://www.vba.vic.gov.au/__data/assets/file/0004/161572/20240067-Raw-Data-December-2023.xlsb"
response = requests.get(buildings_excel)

# Read the content of the file and store it into a dataframe
xlsb_data = BytesIO(response.content)
buildings_df = pd.read_excel(xlsb_data, sheet_name='Data', engine='pyxlsb')

# Convert data frame to csv 
buildings_df.to_csv('../data/landing/building_types_data.csv', index=False)

print("Building Types Data has been downloaded!")
