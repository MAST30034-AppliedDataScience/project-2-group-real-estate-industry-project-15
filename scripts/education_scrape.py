import requests
from bs4 import BeautifulSoup
import csv
import os

############################################ Highschool Rankings Script ###########################################
# setting the URL
url = "https://schoolsfinders.com/victoria-high-school-ranking/"

# setting headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# sending request to website
response = requests.get(url, headers=headers)

# setting the directory path to where the data is saved
directory = "../project-2-group-real-estate-industry-project-15/data/landing"

# making sure directory exists
if not os.path.exists(directory):
    os.makedirs(directory)

# path for the CSV file
csv_file_path = os.path.join(directory, 'VIC_high_school_rankings.csv')

# checking if the request was successful
if response.status_code == 200:
    # parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # finding the table
    heading_div = soup.find('div', class_='elementor-widget-heading')

    if heading_div:
        table = heading_div.find_next('table')

        # making sure the table is found
        if table:
            # extract headers 
            headers = [header.text.strip() for header in table.find_all('th')]

            # extract table rows
            rows = []
            for row in table.find_all('tr')[1:]:
                columns = [col.text.strip() for col in row.find_all('td')]
                rows.append(columns)

            # save data as CSV file 
            with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(rows)

            print(f"Data has been saved to {csv_file_path}")
        else:
            print("Table not found in the page content.")
    else:
        print("The heading division before the table was not found.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
####################################################################################################################



############################################ Primary School Rankings Script ########################################
# setting the URL
url = "https://bettereducation.com.au/school/Primary/vic/vic_top_primary_schools.aspx"

# set headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.get(url, headers=headers)

# setting the directory path to where the data is saved
directory = "../project-2-group-real-estate-industry-project-15/data/landing"

# making sure directory exists
if not os.path.exists(directory):
    os.makedirs(directory)

# csv file path
csv_file_path = os.path.join(directory, 'VIC_primary_school_rankings.csv')

# check if the request was successful
if response.status_code == 200:
    # validate content type
    if 'text/html' in response.headers['Content-Type']:
        # parse the HTML content 
        soup = BeautifulSoup(response.content, 'html.parser')

        # find table containing the school data
        table = soup.find('table', {'class': 'table table-striped table-bordered table-hover'})

        # ensure the table is found
        if table:
            # extract table headers
            headers = [header.text.strip() for header in table.find_all('th')]

            # extract table rows
            rows = []
            for row in table.find_all('tr')[1:]:  # Skipping the header row
                columns = [col.text.strip() for col in row.find_all('td')]
                rows.append(columns)

            # save the data into a CSV 
            with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(rows)

            print(f"Data has been saved to {csv_file_path}")
        else:
            print("Table not found in the page content.")
    else:
        print("Unexpected content type:", response.headers['Content-Type'])
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
###################################################################################################################



############################################ TAFE Locations Script ################################################
# setting url
url = "https://www.vic.gov.au/find-my-local-tafe"

# set headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# sending request to website
response = requests.get(url, headers=headers)

# define directory path
directory = "../project-2-group-real-estate-industry-project-15/data/landing"

if not os.path.exists(directory):
    os.makedirs(directory)

# setting path for csv file
csv_file_path = os.path.join(directory, 'TAFE_locations.csv')

# checking if the request was successful
if response.status_code == 200:
    # parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # find container with the ID 'accordion-2276219'
    accordion_container = soup.find('div', id='accordion-2276219')

    if accordion_container:
        # find all <li> items within the accordion
        tafe_list_items = accordion_container.find_all('li', class_='rpl-accordion__item')

        if tafe_list_items:
            # create list to hold data
            tafe_data = []

            for tafe_item in tafe_list_items:
                # extract the TAFE institute name from the button tag
                institute_name = tafe_item.find('span', class_='rpl-accordion__item-heading-wrapper')
                if institute_name:
                    institute_name = institute_name.text.strip()
                else:
                    institute_name = "Unnamed Institute"

                # extract locations from the corresponding div
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

            # save data into a CSV file
            with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Institute Name', 'Locations'])

                for data in tafe_data:
                    # write the institute name and locations as a single row
                    writer.writerow([data['Institute Name'], "; ".join(data['Locations'])])

            print(f"Data has been saved to {csv_file_path}")
        else:
            print("No TAFE items found in the page content.")
    else:
        print("Accordion container not found in the page content.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

####################################################################################################################


############################################ Primary Secondary School Locations Download ###########################
# setting the URL with the data
url = "https://www.education.vic.gov.au/Documents/about/research/datavic/dv346-schoollocations2023.csv"

# setting file directory
directory = "../project-2-group-real-estate-industry-project-15/data/landing"  # Adjust the path to be in the same hierarchy as the scripts folder

# making sure directory exists
if not os.path.exists(directory):
    os.makedirs(directory)

# define path where the data is to be saved
file_path = os.path.join(directory, "2023_primary_secondary_locations.csv")

# download the data
response = requests.get(url)

# save the contents to a file
with open(file_path, 'wb') as file:
    file.write(response.content)

print(f"File downloaded and saved to {file_path}")
####################################################################################################################

############################################ University Locations Download #########################################
# download from this link and manually move into ../data/landing folder using link below
# https://drive.google.com/file/d/1QjjAcr1DCn_mv6fpZXqFwNWGziAoHHYT/view?usp=sharing
####################################################################################################################

############################################ 2024 Government Primary Secondary School Zones Download ###############
# download from this link and manually move into ../data/landing folder using link below
# https://drive.google.com/drive/folders/1nyHvBrIJ2sAxyDtPM2Ia1YLR-qAV-WX_?usp=sharing
####################################################################################################################