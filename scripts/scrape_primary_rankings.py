import requests
from bs4 import BeautifulSoup
import csv

# define the URL of the page to scrape
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
