import re
import json
from tqdm import tqdm
from collections import defaultdict
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import time
import logging

# Constants
BASE_URL = "https://www.domain.com.au"
N_PAGES = range(1, 5)  # Adjust as needed

# Initialize data structures
url_links = []
property_metadata = defaultdict(dict)

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Generate list of URLs to visit
for page in N_PAGES:
    url = f"{BASE_URL}/rent/melbourne-region-vic/?sort=price-desc&page={page}"
    logger.info(f"Visiting {url}")

    try:
        response = urlopen(Request(url, headers={'User-Agent':"PostmanRuntime/7.6.0"}))
        bs_object = BeautifulSoup(response, "lxml")

        # Attempt to find property links in a different way
        property_cards = bs_object.findAll("li", {"data-testid": "result-card"})
        for card in property_cards:
            link_tag = card.find("a", href=True)
            if link_tag:
                full_url = BASE_URL + link_tag['href'] if not link_tag['href'].startswith(BASE_URL) else link_tag['href']
                if full_url not in url_links:
                    url_links.append(full_url)

    except Exception as e:
        logger.error(f"Error accessing {url}: {e}")
        continue

if not url_links:
    logger.warning("No property links found.")
else:
    logger.info(f"Found {len(url_links)} property links.")

# Scrape data from each property URL
pbar = tqdm(url_links)
success_count, total_count = 0, 0
for property_url in pbar:
    try:
        response = urlopen(Request(property_url, headers={'User-Agent':"PostmanRuntime/7.6.0"}))
        bs_object = BeautifulSoup(response, "lxml")
        total_count += 1

        # Extract property name
        name_tag = bs_object.find("h1", {"class": "css-164r41r"})
        property_metadata[property_url]['name'] = name_tag.get_text(strip=True) if name_tag else "N/A"

        # Extract cost
        cost_tag = bs_object.find("div", {"data-testid": "listing-details__summary-title"})
        property_metadata[property_url]['cost_text'] = cost_tag.get_text(strip=True) if cost_tag else "N/A"

        # Extract rooms and parking
        features_container = bs_object.find("div", {"data-testid": "property-features"})
        if features_container:
            features = features_container.findAll("span", {"data-testid": "property-features-text-container"})
            property_metadata[property_url]['rooms'] = [
                re.findall(r'\d+\s[A-Za-z]+', feature.text)[0] for feature in features
                if 'Bed' in feature.text or 'Bath' in feature.text
            ]
            property_metadata[property_url]['parking'] = [
                re.findall(r'\S+\s[A-Za-z]+', feature.text)[0] for feature in features
                if 'Parking' in feature.text
            ]
        else:
            property_metadata[property_url]['rooms'] = []
            property_metadata[property_url]['parking'] = []

        # Extract description
        desc_tag = bs_object.find("p")
        property_metadata[property_url]['desc'] = desc_tag.get_text(strip=True) if desc_tag else "N/A"

        success_count += 1

    except Exception as e:
        logger.error(f"Error processing {property_url}: {e}")

    pbar.set_description(f"{(success_count/total_count * 100):.0f}% successful")
    time.sleep(1)  # Sleep to avoid overwhelming the server

# Save the output
output_file = '../data/raw/rentals.json'
with open(output_file, 'w') as f:
    json.dump(property_metadata, f, indent=4)

logger.info(f"Data saved to {output_file}")

