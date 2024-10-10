# Datasets
Please provide a high level `README.md` for your chosen datasets

Please find below links to all the datasets we utilised along with instructions on how to retrieve them to run our notebooks and models. 

## Rental History
- [2000 - 2024 Median Rental History by Quarters](https://data.aurin.org.au/dataset/au-govt-abs-sa2-2016-aust-na)
  - Please run the `rental_history_scrape.py` script to download all the relevant data for each property type into the `\data\landing` directory. 

## Income
These are the links and instructions for the datasets we used in our income analysis. 
- [2016 SA2 Codes and Names](https://data.aurin.org.au/dataset/au-govt-abs-sa2-2016-aust-na)

- [2016 Census data](https://www.abs.gov.au/census/find-census-data/datapacks/download/2016_GCP_SA2_for_VIC_short-header.zip)
  - Under the `2016 Census GCP Statistical Area 2 for VIC` folder, find `2016Census_G29_VIC_SA2.csv` for the 2016 income data

- [2021 Census data](https://www.abs.gov.au/census/find-census-data/datapacks/download/2021_GCP_SA2_for_VIC_short-header.zip)
  - Under the `2021 Census GCP Statistical Area 2 for VIC` folder, find `2021Census_G33_VIC_SA2.csv` for the 2021 income data
  - Under the `Metadata` folder, we renamed `2021Census_geog_desc_1st_2nd_3rd_release.xlsx` to `SA2_codes_2021.xlsx`

<br>

## Urban Landmarks 
- [OpenStreetMap (OSM) Data for Australia Sub Region](https://download.geofabrik.de/australia-oceania.html)
  - On the webpage, under the `Sub Regions` heading, we downloaded the `.shp.zip` file from the Australia sub region.
  - For ease of access we have provided the relevant shape files in our Google drive under the folder named `OSM Data Files`. Please download this folder (as a whole) into the `\data\map` directory. 