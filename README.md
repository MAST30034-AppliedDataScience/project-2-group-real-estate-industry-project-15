# Real Estate Consulting Project - Group 15

### Welcome to the Group 15 Industry Project Repository!

### *Project Aim* 
Forecast the median rental prices in Victoria for the next three years (2025-2027) using a range of engineered features identified as relevant predictors. Additionally, we aim to identify the most important internal and external features influencing rental prices and highlight the top 10 growth suburbs.

<br>

### *Instructions to Run the Code* 
The following steps outline how to run our code:

#### 1. *Download all Required Libraries* 
Before running our code, please ensure you’ve read our `requirements.txt` file and have downloaded all of the necessary libraries.

To install the required packages while in the root directory:
```
pip install -r requirements.txt
```

#### 2. *API Keys*
For the [OpenRouteService](https://openrouteservice.org/) API, register for an account and create an API key to access the location-based services. The generated API key should then be saved into a file named `api.env` into the root directory of the project.


#### 3. *Run All Notebooks in the Repository:*
1. Run all the files under the scripts directory in order to obtain the necessary datasets.
2. Access each notebook in the `preprocessing` folder, follow the specific instructions as outlined at the top of the notebook in the **PLEASE READ: DATA DOWNLOAD** section to download the required datasets from our [Google Drive](https://drive.google.com/drive/folders/1JzqWIVPAHOvMeD0X1u3RefYBSj1PehZ0?usp=sharing).
    - Note that only UniMelb accounts are able to access the Google Drive.
3. Run all the notebooks in the `preprocessing` folder, located in the `notebooks` directory.
4. Access the `modelling.ipynb` notebook located in the `models` folder. 
    - Follow the data download instructions outlined in the **PLEASE READ: DATA DOWNLOAD** section of that notebook. 
    - **MUST** download the feature sets from the [Google Drive](https://drive.google.com/drive/folders/1JzqWIVPAHOvMeD0X1u3RefYBSj1PehZ0?usp=sharing).
    - To obtain the same results as we did for the modelling, it would be best to use the same data from our Google Drive, specifically for the scraped Domain data.
5. Run the the `modelling.ipynb` notebook.
    - Please note this notebook takes around 30 minutes to run. 
5. Run all the notebooks in the `notebooks/analyses/` directory.
6. Run all the notebooks in the `notebooks/feature_eng` directory.
7. Finally, run the `analysis_rental_predictions.ipynb` notebook located in the `models` directory.
    - Follow the instructions in the RENT VISION PRO USAGE section to modify the specific suburb and property type examined in the Rent Vision Pro Tool. 

<br>

### *Other Relevant Files:*
- Our `summary.ipynb` and `assumptions.ipynb` notebooks are located in the `notebooks` directory.
- Our data `README` file is located in the `data` folder.
