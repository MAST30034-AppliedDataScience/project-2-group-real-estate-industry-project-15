# Downloading the population extrernal dataset using API

from owslib.wfs import WebFeatureService
import pandas as pd 
import geopandas
import folium
import io
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

WFS_USERNAME = 'kathleenfiona.wongso@student.unimelb.edu.au'
WFS_PASSWORD= 'eyJzdWIiOiI4NmVjZTlmNy0wZTI5LTQzNzMtYmM1Zi03ZmU3N2ZjMDNjOTAiLCJjaGsiOiI3ODM1NGE1MyIsImV4cCI6MTczMjc2NDk0Nn0.YIt2Sca5iJvVbANz7NHFqDiCAFLoazwyvyLHqnSGnss'
WFS_URL='https://adp.aurin.org.au/geoserver/wfs'

api_client = WebFeatureService(url=WFS_URL,username=WFS_USERNAME, password=WFS_PASSWORD, version='1.1.0')

response = api_client.getfeature(typename='datasource-AU_Govt_ABS-UoM_AURIN_DB_3:abs_regional_population_sa2_2001_2021', outputFormat='csv')

out = open('../data/landing/population.csv', 'wb')
out.write(response.read())
out.close()