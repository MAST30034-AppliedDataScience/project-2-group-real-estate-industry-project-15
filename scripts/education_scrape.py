import requests
from bs4 import BeautifulSoup
import csv




############################################ Highschool Rankings Script ############################################
# define URL
url = "https://schoolsfinders.com/victoria-high-school-ranking/"

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

    # locate the table
    # search for the div class just before the table
    heading_div = soup.find('div', class_='elementor-widget-heading')
    
    if heading_div:
        # the table should be near or after this div
        table = heading_div.find_next('table')

        # ensure table is found
        if table:
            # extract table headers
            headers = [header.text.strip() for header in table.find_all('th')]

            # extract table rows
            rows = []
            for row in table.find_all('tr')[1:]:  # skip header row
                columns = [col.text.strip() for col in row.find_all('td')]
                rows.append(columns)

            # save the data into a CSV file
            with open('victoria_high_school_rankings.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(rows)

            print("Data has been saved to victoria_high_school_rankings.csv")
        else:
            print("Table not found in the page content.")
    else:
        print("The heading division before the table was not found.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
####################################################################################################################



############################################ Primary School Rankings Script ########################################
# define the URL
url = "https://bettereducation.com.au/school/Primary/vic/vic_top_primary_schools.aspx"

# set headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# send get request to website
response = requests.get(url, headers=headers)

# check if the request was successful
if response.status_code == 200:
    # validate content type
    if 'text/html' in response.headers['Content-Type']:
        # parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # find table containing the school data
        table = soup.find('table', {'class': 'table table-striped table-bordered table-hover'})

        # ensure the table is found
        if table:
            # extract the table headers
            headers = [header.text.strip() for header in table.find_all('th')]

            # extract the table rows
            rows = []
            for row in table.find_all('tr')[1:]:  # Skipping the header row
                columns = [col.text.strip() for col in row.find_all('td')]
                rows.append(columns)

            # save the data into a CSV file
            with open('vic_top_primary_schools.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(rows)

            print("Data has been saved to vic_top_primary_schools.csv")
        else:
            print("Table not found in the page content.")
    else:
        print("Unexpected content type:", response.headers['Content-Type'])
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

####################################################################################################################



############################################ TAFE Locations Script ################################################
# define URL
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

####################################################################################################################


############################################ Primary School Locations Download #####################################

####################################################################################################################

############################################ Secondary School Locations Download ###################################

####################################################################################################################

############################################ Government Primary School Zones Download ##############################

####################################################################################################################

############################################ Government Secondary School Zones Download ############################

####################################################################################################################

############################################ University Locations Download #########################################

####################################################################################################################