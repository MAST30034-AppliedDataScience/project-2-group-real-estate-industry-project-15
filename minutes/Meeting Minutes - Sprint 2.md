# Meeting 2 (30 Aug 2024\)

**Project Title: Real Estate Industry Project**

Minutes (30 August 2024, Friday 1pm)			

**Group Members:**

- Mokshith Setty (1180580)  
- Xiangxi Cheng (1270419)  
- Saleha Khalid (1122166)  
- Kathleen Fiona Wongso (1343015)  
- Proma Ali (1268794) 			

**Agenda:**	

![][image1]

- [x] Begin scraping data from the real estate website   
- [x] Confirm the external datasets  
      - [x] Write up how we’re going to extract that data and what features will be used   
- [x] Create a map based on the victorian suburbs 

**Signed:** 

Mokshith (30/8), Saleha (30/8), Xiangxi (30/8), Kathleen (30/8), Proma (30/8)	

---

**Scraping Data from the Real Estate Website** 

We have begun scraping the data from the real estate website as evident in our ‘rental\_scrape.py’ script in the scripts folder. We utilisied the skeleton code while including additional features we deemed to be relevant. These additional features include \- property type, bond, property features and property description. Our next step is to extract all property data based on our timeframe as well as deciding how many pages of property data/number of properties we require. 

**EXTERNAL DATASETS**

| External Dataset  | Data Retrieval Method | Relevant Features | Person in Charge |
| ----- | ----- | ----- | ----- |
| Building Types in Each Suburb (Signifying retail, commercial, residential etc. spaces in the area) [https://discover.data.vic.gov.au/dataset/building-permit-activity-data-2023](https://discover.data.vic.gov.au/dataset/building-permit-activity-data-2023) | Download the excel file from the website and store it in a google drive link.   | Street name, suburb, postcode, municipality \- we can turn these into longitude and latitude —- Building use description \- indicates if the building is retail, commercial, public building or domestic. | Proma  |
| Crime data set from Crime Statistics Agency  2023 \- [https://files.crimestatistics.vic.gov.au/2024-06/Data\_Tables\_LGA\_Recorded\_Offences\_Year\_Ending\_December\_2023\_0.xlsx](https://files.crimestatistics.vic.gov.au/2024-06/Data\_Tables\_LGA\_Recorded\_Offences\_Year\_Ending\_December\_2023\_0.xlsx) 2022 \-  [https://files.crimestatistics.vic.gov.au/2023-03/Data\_Tables\_LGA\_Recorded\_Offences\_Year\_Ending\_December\_2022.xlsx](https://files.crimestatistics.vic.gov.au/2023-03/Data\_Tables\_LGA\_Recorded\_Offences\_Year\_Ending\_December\_2022.xlsx) 2021 \-  https://files.crimestatistics.vic.gov.au/2022-03/Data\_Tables\_LGA\_Recorded\_Offences\_Year\_Ending\_December\_2021.xlsx | Data will be collected from Crime Statistics Agency. We can retrive it via the URL and we get them in the form of excel files | Year, Suburb, Offence Division, Offence subdivision, Offence subgroup, Offence Count | Mok |
| Education (Primary/Secondary/Tertiary) Locations & Ranking School locations: [https://www.education.vic.gov.au/Documents/about/research/datavic/dv346-schoollocations2023.csv](https://www.education.vic.gov.au/Documents/about/research/datavic/dv346-schoollocations2023.csv) (change year in link for 202x dataset) Gov school zones:[https://www.education.vic.gov.au/Documents/about/research/datavic/dv330-schoolzones2023.zip](https://www.education.vic.gov.au/Documents/about/research/datavic/dv330-schoolzones2023.zip) Secondary school rankings:[https://bettereducation.com.au/school/Secondary/vic/vic\_top\_secondary\_schools.aspx](https://bettereducation.com.au/school/Secondary/vic/vic\_top\_secondary\_schools.aspx) Uni and TAFE: im working on it | School Locations: primary & secondary: Download CSV from Education.vic.gov Government School Zones: Junior & Senior school: Download Zip from Education.vic.gov School Rankings: Scrape data from Better Education website (primary done, secondary to go) Tertiary Education Locations: Collect dataset manually from official websites?  | School location: School\_name, School\_type, LGA\_ID and Name, XY coordinates School Rankings: Ranking, Post code, Total enrollments? | Xiangxi (Melissa) |
| Population per SA2 [https://www.abs.gov.au/statistics/people/population/regional-population/2022-23/32180DS0001\_2022-23.xlsx](https://www.abs.gov.au/statistics/people/population/regional-population/2022-23/32180DS0001\_2022-23.xlsx) | Download directly from the link provided, or by running Python script under scripts directory | Estimated population & population density, births, deaths, net migration (internal and overseas) | Kathleen Note: ended up changing source due to outdated SA2 names and codes |
| Income per SA2 [https://digital.atlas.gov.au/datasets/digitalatlas::abs-income-including-government-allowances-by-2021-sa2-nov-2023/about](https://digital.atlas.gov.au/datasets/digitalatlas::abs-income-including-government-allowances-by-2021-sa2-nov-2023/about)  | Downloaded directly from digital.atlas.gov.au (no credentials required) | Personal income; income inequality measures; government pensions and allowances | Kathleen |
| Covid-19 [https://discover.data.vic.gov.au/dataset/all-victorian-sars-cov-2-cases-by-local-government-area-and-postcode](https://discover.data.vic.gov.au/dataset/all-victorian-sars-cov-2-cases-by-local-government-area-and-postcode)  | Downloaded directly from data.vic.gov | Timestamps, post code, LGA, total count of cases | Saleha |
| PTV Data \- Trains (Metro & Regional) and Trams (Metro) | Download shapefiles from [https://discover.data.vic.gov.au/dataset/ptv-metro-train-stations](https://discover.data.vic.gov.au/dataset/ptv-metro-train-stations) [https://discover.data.vic.gov.au/dataset/ptv-regional-train-stations](https://discover.data.vic.gov.au/dataset/ptv-regional-train-stations) [https://discover.data.vic.gov.au/dataset/ptv-metro-tram-stops](https://discover.data.vic.gov.au/dataset/ptv-metro-tram-stops)   | Train and tram locations  | Proma  |

**VISUALISING THE GEOLOCATION OF THE PROPERTIES**

\* Code for this is in the *playground.ipynb* in our repository. 

| File | Link  |
| :---- | :---- |
| Shapefile of suburbs  | [https://data.gov.au/dataset/ds-dga-af33dd8c-0534-4e18-9245-fc64440f742e/details](https://data.gov.au/dataset/ds-dga-af33dd8c-0534-4e18-9245-fc64440f742e/details) |
| Shapefile of SA2 areas | [https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files](https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files)  |

We created an interactive map displaying the suburbs in Victoria. The map is interactive hence if one person hovers over the suburb area, the name of the suburb appears. We will use this map to view the distribution of rental properties across victoria. 

# Meeting 3 (3 Sep 2024\)

**Project Title: Real Estate Industry Project**

Minutes (3 September 2024, Friday 1pm)			

**Group Members:**

- Mokshith Setty (1180580)  
- Xiangxi Cheng (1270419)  
- Saleha Khalid (1122166)  
- Kathleen Fiona Wongso (1343015)  
- Proma Ali (1268794) 			

**Agenda:**	

![][image2]

- [x] Finish scraping and saving rental data from the real estate website   
      - [x] Finalise the features we will use for each rental property  
      - [x] Finalise the number of rental properties we will use   
- [x] Use SA2 to derive population forecast and affluence   
- [x] Begin scraping our respective external datasets 

**Signed:** 

Mokshith (3/9), Saleha (3/9), Xiangxi (3/9), Kathleen (3/9), Proma (3/9)	

---

# Scraping Rental Domain.com Properties (as of W7)

## Scraping Methodology

* Scrape properties based on the Victoria postcode: 3000 \- 3999  
* We went through every single page and found the corresponding properties relating to each postcode.   
* We also ensured with a few checks that the number of properties we scraped matched the number of properties on the website for the respective postcode.   
* Saved in “scraped\_properties.json” in our repository   
  * 10 mb

## Features 

* Address (string)  
* Bond (for those that don’t specify, we assume one month’s worth \- even if \> $900)  
* Price (string containing the frequency of the rental price)  
* Rooms (string)  
* Parking (string)  
* Additional Features (string)   
* Availability (timestamp)  
* Property Type (string)  
* Coordinates

### Preprocessing Notes

* Split rooms into bedrooms and bathrooms  
* Remove property description as it is just fluff  
* Make sure all rental prices are in the same format (e.g. $500 weekly rather than $2k monthly)  
* Additional Features \- some features have ‘\*’ after or before the text. Remove this. 

## No. of Properties Scraped

* We extracted every single property that is posted for rent in Victoria on 03/09/2024  
  * 14076 Properties for rent in VIC

# Updated External Datasource

* Highschool rankings, scrape data using script: [https://schoolsfinders.com/victoria-high-school-ranking/](https://schoolsfinders.com/victoria-high-school-ranking/) as previous data from better education only includes evaluation based on years 7-10. Highschool rankings should consider VCE scores.   
* TAFE locations from here, scrape data using script: [https://www.vic.gov.au/find-my-local-tafe](https://www.vic.gov.au/find-my-local-tafe)  
* Rental Report \- Quarterly medians [https://discover.data.vic.gov.au/dataset/rental-report-quarterly-quarterly-median-rents-by-lg](https://discover.data.vic.gov.au/dataset/rental-report-quarterly-quarterly-median-rents-by-lga)a   
* University locations from here, T\&C’s from website prohibit automated scraping of data but allows copies to be made for non-commercial purposes, hence will be collected manually into CSVs: [https://universityreviews.com.au/list-of-universities/victoria/\#google\_vignette](https://universityreviews.com.au/list-of-universities/victoria/\#google\_vignette)  
  And saved to google docs link here: [https://drive.google.com/file/d/1D432NwL6SSUs5zG\_ZMDjG4CYq2JT4MNO/view?usp=sharing](https://drive.google.com/file/d/1D432NwL6SSUs5zG\_ZMDjG4CYq2JT4MNO/view?usp=sharing)  
* Population forecast: [https://www.planning.vic.gov.au/\_\_data/assets/excel\_doc/0028/691660/VIF2023\_SA2\_Pop\_Hhold\_Dwelling\_Projections\_to\_2036\_Release\_2.xlsx](https://www.planning.vic.gov.au/\_\_data/assets/excel\_doc/0028/691660/VIF2023\_SA2\_Pop\_Hhold\_Dwelling\_Projections\_to\_2036\_Release\_2.xlsx) 

| Name | Data Downloaded/Scraped |
| ----- | ----- |
| Proma | Shopping Centre Data  Sports & Recreational Facilities  Parks & Conservation Areas Building Types Data  Public Transport ShapeFiles  |
| Xiangxi | TAFE Locations (CSV) VIC Top Primary School Rankings (CSV) VIC Top High School Rankings (CSV) Primary School Locations (CSV) Secondary School Locations (CSV) University Locations (CSV) GOV Primary School Zones ShapeFiles GOV Secondary School Zones ShapeFiles  |
| Kathleen | Demographics (CSV Files) Population per SA2 (scraped using Python script)  Income per SA2 (will upload google drive link as the website does not allow scraping) Made Jupyter notebook to preprocess and merged income and population datasets into one file |
| Mokshith | Crime Saved crime data into a parquet file (downloaded as excel file and saved as parquet) WIll be converted into csv after preprocessing |
| Saleha | Fix the rental scraping data  Include coordinates for rentals & add retries to code for server error Saved all rental data into a JSON file Median rental pricing history for suburbs (CSV) Saved as CSV for all types of properties from 1br flat \- 4br house & all properties |

# Use SA2 to Derive Population Forecast & Affluence 

## SA2 Population Forecast 

To derive the population forecast, we found a dataset by planning Victoria which has estimated the population per SA2 for the years of 2021 \- 2036 in 5 year intervals. We will use this already forecasted data in our analysis. We did not deem it necessary to create a machine learning model to predict this data when Planning Victoria has already forecasted it for us.   
	[https://www.planning.vic.gov.au/\_\_data/assets/excel\_doc/0028/691660/VIF2023\_SA2\_Pop\_Hhold\_Dwelling\_Projections\_to\_2036\_Release\_2.xlsx](https://www.planning.vic.gov.au/\_\_data/assets/excel\_doc/0028/691660/VIF2023\_SA2\_Pop\_Hhold\_Dwelling\_Projections\_to\_2036\_Release\_2.xlsx) 

## SA2 Population Affluence 

As for affluence, in our ‘playground.ipynb’, we have visualised the total median income per SA2 excluding government pensions and allowances. As shown in the map, as we get closer to the CBD, the median income increases. In the rural areas of Victoria, the median income is relatively lower. This aligns with our assumptions and research. We will further enhance this visualisation and connect our findings to how affluence can impact forecasted rental prices in future sprints.   
