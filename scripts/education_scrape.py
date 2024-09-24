import requests
import pandas as pd
from bs4 import BeautifulSoup
from io import BytesIO
import csv
import os

############################################ Highschool School achievements Script #################################
# URL of the file to download
download_link = 'https://www.vcaa.vic.edu.au/Documents/statistics/2023/2023SeniorSecondaryCompletionAndAchievementInformation.xlsx'

# Directory where the CSV file should be saved
save_directory = '../project-2-group-real-estate-industry-project-15/data/landing'
# Ensure the save directory exists
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# Define the CSV file name for saving
csv_file_name = '2023SeniorSecondaryCompletionAndAchievementInformation.csv'

# Full file path for the CSV file
csv_file_path = os.path.join(save_directory, csv_file_name)

# Download the Excel file in memory (no need to save it)
response = requests.get(download_link)

# Check if the download was successful
if response.status_code == 200:
    # Load the Excel file content into a BytesIO object
    # Skip the first 9 rows (meta data) and set the 10th row (index 9) as headers
    excel_data = pd.read_excel(BytesIO(response.content), skiprows=9)

    # Set the second row (after skip) as the header manually
    excel_data.columns = excel_data.iloc[0]  # Use the first row of the dataframe as the header
    excel_data = excel_data[1:]  # Remove the row that we used as header

    # Convert the cleaned dataframe to CSV and save it
    excel_data.to_csv(csv_file_path, index=False)

    print(f'Excel file has been converted to CSV (with the correct headers) and saved as {csv_file_path}')
else:
    print(f'Failed to download the file. Status code: {response.status_code}')

####################################################################################################################


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


############################################# Sedondary School Enrollments Download ################################
# Step 1: Set the URL for the data
url = "https://www.education.vic.gov.au/Documents/about/research/datavic/dv355-VIC%20All%20Schools%20Enrolments%202023.csv"

# Step 2: Set the file directory
directory = "../project-2-group-real-estate-industry-project-15/data/landing"  # Adjust the path according to your project structure

# Step 3: Ensure the directory exists, if not, create it
if not os.path.exists(directory):
    os.makedirs(directory)

# Step 4: Define the file path where the data will be saved
file_path = os.path.join(directory, "All_schools_enrollments.csv")

# Step 5: Download the data
response = requests.get(url)

# Step 6: Check if the download was successful (status code 200)
if response.status_code == 200:
    # Step 7: Save the contents to a file
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print(f"File downloaded and saved to {file_path}")
else:
    print(f"Failed to download the file. Status code: {response.status_code}")
####################################################################################################################