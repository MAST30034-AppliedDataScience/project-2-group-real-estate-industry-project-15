import requests
from bs4 import BeautifulSoup
import csv

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
