# Import Libraries 
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Retrieve the content from the URL
url = "https://www.matthewproctor.com/full_australian_postcodes_vic"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table which stores the postcodes and suburb names
table = soup.find('table')

# Extract the data from the table rows
suburb_data = []
# Skip header
for row in table.find_all('tr')[1:]: 
    cells = row.find_all('td')
    if len(cells) >= 3:  
        # Postcode is 2nd col and suburb name is 3rd col
        postcode = cells[1].text.strip()  
        suburb = cells[2].text.strip().title()  # Convert to Title Case
        longitude = cells[4].text.strip() 
        latitude = cells[5].text.strip() 
        suburb_data.append({'Postcode': postcode, 'Suburb': suburb, 'Longitude': longitude, 'Latitude': latitude})

# Created data frame 
df = pd.DataFrame(suburb_data, columns=['Postcode', 'Suburb', 'Longitude', 'Latitude'])

# Save to CSV
df.to_csv('../data/landing/VIC_Suburbs.csv', index=False)