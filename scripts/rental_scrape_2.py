############################################## Suburb Name & Postcode Data ##############################################
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
        suburb_data.append({'Postcode': postcode, 'Suburb': suburb})

# Created data frame 
df = pd.DataFrame(suburb_data, columns=['Postcode', 'Suburb'])

# Save to CSV
df.to_csv('../data/landing/VIC_Postcodes.csv', index=False)


############################################## Rental Scraping ##############################################
# built-in imports
import re
from json import dump
from tqdm import tqdm
from collections import defaultdict
import urllib.request
from urllib.parse import urlparse, parse_qs
from time import sleep
import urllib.error
import pandas as pd

# user packages
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

# Constants
BASE_URL = "https://www.oldlistings.com.au/real-estate"
MAX_RETRIES = 3  # Number of retries
RETRY_DELAY = 5  # Delay between retries in seconds

# Load postcodes and suburbs from a CSV file
csv_file_path = "../data/landing/VIC_Postcodes.csv"  # Replace with your actual file path
suburbs_data = pd.read_csv(csv_file_path)

# Define custom headers to mimic a real browser request
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com',
    'Connection': 'keep-alive'
}

# Begin code
property_metadata = []

# Generate list of URLs to visit
for index, row in suburbs_data.iterrows():
    suburb = row['Suburb'].replace(" ", "+")
    postcode = row['Postcode']
    page_number = 1
    
    while True:
        # Construct URL for each page of the suburb and postcode
        if page_number == 1:
            url = f"{BASE_URL}/VIC/{suburb}/{postcode}/rent/"
        else:
            url = f"{BASE_URL}/VIC/{suburb}/{postcode}/rent/{page_number}"
        
        print(f"Visiting {url}")
        
        try:
            req = Request(url, headers=HEADERS)  # Use enhanced headers
            bs_object = BeautifulSoup(urlopen(req), "lxml")
            print(f"Successfully fetched URL: {url}")  # Debugging print
        except urllib.error.HTTPError as e:
            print(f"Error fetching {url}: {e}")
            break
        except Exception as e:
            print(f"General error fetching {url}: {e}")
            break

        # Find the section containing all properties
        properties_section = bs_object.find("section", class_=re.compile(r"grid-\d+ pull-\d+"))
        if not properties_section:
            print(f"No properties found in URL: {url}")
            break
        
        # Extract all properties from the section
        property_listings = properties_section.find_all("div", class_="property odd clearfix")
        
        if not property_listings:
            print(f"No more properties found for URL: {url}")
            break
        
        # Process each property listing
        for property_div in property_listings:
            # Initialize a dictionary to store property details
            property_data = {}
            
            # Extract property details
            parent_section = property_div.find_parent("section", class_="grid-100 grid-parent")

            if parent_section:
                # Address
                address_element = parent_section.find("h2", class_="address")
                property_data['address'] = address_element.text.strip() if address_element else 'Not available'

                # Property details: beds, baths, type
                bed_element = parent_section.find("p", class_="property-meta bed")
                bath_element = parent_section.find("p", class_="property-meta bath")
                type_element = parent_section.find("p", class_="property-meta type")
                
                property_data['beds'] = bed_element.text.strip() if bed_element else 'Not available'
                property_data['baths'] = bath_element.text.strip() if bath_element else 'Not available'
                property_data['type'] = type_element.text.strip() if type_element else 'Not available'

                # Last advertised price and date
                price_section = parent_section.find("section", class_="grid-35 tablet-grid-35 price")
                if price_section:
                    last_advertised_price_date = price_section.find("span").text.strip()
                    last_advertised_price = price_section.find("h3").text.strip()
                    property_data['last_advertised_price_date'] = last_advertised_price_date.replace("Last Advertised Price : ", "").strip()
                    property_data['last_advertised_price'] = last_advertised_price
                else:
                    property_data['last_advertised_price_date'] = 'Not available'
                    property_data['last_advertised_price'] = 'Not available'
                
                # Historical prices
                historical_prices_section = parent_section.find("section", class_="grid-100 historical-price")
                historical_prices = []
                if historical_prices_section:
                    historical_list_items = historical_prices_section.find_all("li")
                    for item in historical_list_items:
                        span_elements = item.find_all("span")
                        if len(span_elements) == 2:
                            historical_prices.append({
                                'date': span_elements[0].text.strip(),
                                'price': span_elements[1].text.strip()
                            })
                property_data['historical_prices'] = historical_prices

            # Add the property data to the list
            property_metadata.append(property_data)
            print(f"Extracted property data: {property_data}")  # Debugging print

        # Increment to check the next page
        page_number += 1

# Check if any properties were collected
print(f"Total properties scraped: {len(property_metadata)}")

# Output scraped data into a file
with open('../data/landing/scraped_properties.json', 'w') as f:
    dump(property_metadata, f, indent=4)

print("Scraping completed and data saved.")
