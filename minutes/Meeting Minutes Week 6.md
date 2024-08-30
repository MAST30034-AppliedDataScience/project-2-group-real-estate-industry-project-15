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
| Population per SA2 [https://adp-access.aurin.org.au/dataset/au-govt-abs-abs-regional-population-sa2-2001-2021-sa2-2016](https://adp-access.aurin.org.au/dataset/au-govt-abs-abs-regional-population-sa2-2001-2021-sa2-2016)  | Original dataset from the ABS but downloaded from aurin.org.au, (can download directly by using UniMelb credentials, or by using API) | Estimated population & population density, births, deaths, net migration (internal and overseas) | Kathleen |
| Income per SA2 [https://digital.atlas.gov.au/datasets/digitalatlas::abs-income-including-government-allowances-by-2021-sa2-nov-2023/about](https://digital.atlas.gov.au/datasets/digitalatlas::abs-income-including-government-allowances-by-2021-sa2-nov-2023/about)  | Downloaded directly from digital.atlas.gov.au (no credentials required) | Personal income; income inequality measures; government pensions and allowances | Kathleen |
| Covid-19 [https://discover.data.vic.gov.au/dataset/all-victorian-sars-cov-2-cases-by-local-government-area-and-postcode](https://discover.data.vic.gov.au/dataset/all-victorian-sars-cov-2-cases-by-local-government-area-and-postcode)  | Downloaded directly from data.vic.gov | Timestamps, post code, LGA, total count of cases | Saleha |
| PTV Data \- Trains (Metro & Regional) and Trams (Metro) | Download shapefiles from [https://discover.data.vic.gov.au/dataset/ptv-metro-train-stations](https://discover.data.vic.gov.au/dataset/ptv-metro-train-stations) [https://discover.data.vic.gov.au/dataset/ptv-regional-train-stations](https://discover.data.vic.gov.au/dataset/ptv-regional-train-stations) [https://discover.data.vic.gov.au/dataset/ptv-metro-tram-stops](https://discover.data.vic.gov.au/dataset/ptv-metro-tram-stops)   | Train and tram locations  | Proma  |

**VISUALISING THE GEOLOCATION OF THE PROPERTIES**

\* Code for this is in the *playground.ipynb* in our repository. 

| File | Link  |
| :---- | :---- |
| Shapefile of suburbs  | [https://data.gov.au/dataset/ds-dga-af33dd8c-0534-4e18-9245-fc64440f742e/details](https://data.gov.au/dataset/ds-dga-af33dd8c-0534-4e18-9245-fc64440f742e/details) |
| Shapefile of SA2 areas | [https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files](https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files)  |

We created an interactive map displaying the suburbs in Victoria (please see the 'plots' folder in our repositary). The map is interactive hence if one person hovers over the suburb area, the name of the suburb appears. We will use this map to view the distribution of rental properties across victoria. 