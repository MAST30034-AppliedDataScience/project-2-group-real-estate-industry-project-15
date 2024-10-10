# built-in imports
import re
from json import dump
from tqdm import tqdm
from collections import defaultdict
import urllib.request
from urllib.parse import urlparse, parse_qs
from time import sleep
import urllib.error

# user packages
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

# constants
BASE_URL = "https://www.domain.com.au"
POSTCODES = range(3000, 4000)
MAX_RETRIES = 3  # Number of retries
RETRY_DELAY = 5  # Delay between retries in seconds

# begin code
url_links = []
property_metadata = defaultdict(dict)

# generate list of urls to visit
for code in POSTCODES:
    page_number = 1
    while True:
        # Construct URL for each page of the postcode
        url = BASE_URL + f"/rent/?postcode={code}&excludedeposittaken=1&sort=default-desc&page={page_number}"
        print(f"Visiting {url}")
        try:
            bs_object = BeautifulSoup(urlopen(Request(url, headers={'User-Agent': "PostmanRuntime/7.6.0"})), "lxml")
        except urllib.error.HTTPError as e:
            print(f"Error fetching {url}: {e}")
            break

        # Find property links on the page
        try:
            index_links = bs_object.find("ul", {"data-testid": "results"}).findAll("a", href=re.compile(f"{BASE_URL}/.*"))
            found_links = False
            for link in index_links:
                # if its a property address, add it to the list
                if 'address' in link.get('class', []):
                    url_links.append(link['href'])
                    found_links = True

            # If no links were found, break out of the loop for this postcode
            if not found_links:
                break

        except AttributeError:
            # If the results list is not found, assume there are no more pages
            break
        
        # Increment to check the next page
        page_number += 1

# for each url, scrape some basic metadata
pbar = tqdm(url_links[1:])
success_count, total_count = 0, 0
for property_url in pbar:
    for attempt in range(MAX_RETRIES):
        try:
            # Fetch property page with retries
            bs_object = BeautifulSoup(urlopen(Request(property_url, headers={'User-Agent': "PostmanRuntime/7.6.0"})), "lxml")
            total_count += 1

            # looks for the header class to get property name
            property_metadata[property_url]['address'] = bs_object.find("h1", {"class": "css-164r41r"}).text

            # looks for the div containing a summary title for cost
            property_metadata[property_url]['rental_price'] = bs_object.find("div", {"data-testid": "listing-details__summary-title"}).text

            # get rooms and parking
            rooms = bs_object.find("div", {"data-testid": "property-features"}).findAll("span", {"data-testid": "property-features-text-container"})

            # rooms
            property_metadata[property_url]['rooms'] = [
                re.findall(r'\d+\s[A-Za-z]+', feature.text)[0] for feature in rooms
                if 'Bed' in feature.text or 'Bath' in feature.text
            ]
            # parking
            property_metadata[property_url]['parking'] = [
                re.findall(r'\S+\s[A-Za-z]+', feature.text)[0] for feature in rooms
                if 'Parking' in feature.text
            ]

            # Extract all property features
            features_section = bs_object.find("div", {"data-testid": "listing-details__additional-features"})
            if features_section:
                features_list = features_section.findAll("li")  # Extract all 'li' elements for features
                property_metadata[property_url]['features'] = [feature.text.strip() for feature in features_list if feature.text.strip()]
            else:
                property_metadata[property_url]['features'] = []  # Keep it empty if no features are found

            # Extract property description
            description = bs_object.find("div", {"data-testid": "listing-details__description"}).find("p")
            property_metadata[property_url]['desc'] = description.text.strip() if description else 'Not available'

            # Extract bond amount and availability from listing summary strip
            summary_strip = bs_object.find("ul", {"data-testid": "listing-summary-strip"})
            if summary_strip:
                summary_items = summary_strip.findAll("li")
                # Loop through summary items to find bond and availability details
                for item in summary_items:
                    text = item.get_text(strip=True)
                    if "Bond" in text:
                        property_metadata[property_url]['bond'] = text.replace('Bond', '').strip()
                    elif "Available" in text:
                        property_metadata[property_url]['availability'] = text.replace('Date Available:', '').strip()

            # Extract property type
            property_type_element = bs_object.find("div", {"data-testid": "listing-summary-property-type"})
            property_metadata[property_url]['property_type'] = property_type_element.text.strip() if property_type_element else 'Not available'

            # Extract coordinates from Google Maps link
            directions_link = bs_object.find("a", href=re.compile(r"https://www.google.com/maps/dir/"))
            if directions_link and 'href' in directions_link.attrs:
                href = directions_link['href']
                parsed_url = urlparse(href)
                query_params = parse_qs(parsed_url.query)
                if 'destination' in query_params:
                    property_metadata[property_url]['coordinates'] = query_params['destination'][0]
                else:
                    property_metadata[property_url]['coordinates'] = 'Not available'
            else:
                property_metadata[property_url]['coordinates'] = 'Not available'

            success_count += 1
            break  # Break out of retry loop if successful

        except urllib.error.HTTPError as e:
            if e.code == 500:
                print(f"HTTP 500 error for {property_url}. Retrying... ({attempt + 1}/{MAX_RETRIES})")
                sleep(RETRY_DELAY)
            else:
                print(f"Failed to retrieve {property_url} due to {e}.")
                break  # Exit if it's not a 500 error
        except Exception as e:
            print(f"General error for {property_url}: {e}")
            break

    pbar.set_description(f"{(success_count / total_count * 100):.0f}% successful")

# output scraped data into a file
with open('../data/landing/scraped_properties.json', 'w') as f:
    dump(property_metadata, f)