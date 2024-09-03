import requests
from bs4 import BeautifulSoup
import csv

# Define URL
url = "https://www.vic.gov.au/find-my-local-tafe"

# set headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# send get request to the website
response = requests.get(url, headers=headers)

# check if the request was successful
if response.status_code == 200:
    # parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # find the container with the ID 'accordion-2276219'
    accordion_container = soup.find('div', id='accordion-2276219')

    if accordion_container:
        # find all <li> items within the accordion
        tafe_list_items = accordion_container.find_all('li', class_='rpl-accordion__item')

        if tafe_list_items:
            # create a list to hold the data
            tafe_data = []

            # loop through each item in the list
            for tafe_item in tafe_list_items:
                # extract the TAFE institute name from the button tag
                institute_name = tafe_item.find('span', class_='rpl-accordion__item-heading-wrapper')
                if institute_name:
                    institute_name = institute_name.text.strip()
                else:
                    institute_name = "Unnamed Institute"

                # extract the locations from the corresponding div
                content_div = tafe_item.find('div', class_='rpl-content rpl-accordion__item-content-inner')
                location_list = []
                if content_div:
                    # check for lists or paragraphs containing location info
                    locations_ul = content_div.find('ul')
                    locations_p = content_div.find_all('p')

                    if locations_ul:
                        # extract list items if locations are in a list
                        location_list = [li.text.strip() for li in locations_ul.find_all('li')]
                    elif locations_p:
                        # extract paragraph text if locations are in paragraphs
                        location_list = [p.text.strip() for p in locations_p]

                # append the data to the list
                tafe_data.append({
                    'Institute Name': institute_name,
                    'Locations': location_list
                })

            # save the data into a CSV file
            with open('tafe_locations.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Institute Name', 'Locations'])

                for data in tafe_data:
                    # write the institute name and locations as a single row
                    writer.writerow([data['Institute Name'], "; ".join(data['Locations'])])

            print("Data has been saved to tafe_locations.csv")
        else:
            print("No TAFE items found in the page content.")
    else:
        print("Accordion container not found in the page content.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
