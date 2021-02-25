import os
import io
import requests
import pandas as pd


def download_covid_csv():
    try:

        CSV_URL = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
        response = requests.get(CSV_URL).content
        path = os.path.join(os.getcwd(), 'covidmap/data_management/csv/owid-covid-data.csv')
        df = pd.read_csv(io.StringIO(response.decode(encoding='utf-8')))
        df.to_csv(path, index=False)
        print('File updated.')
        
        return path
    
    except requests.ConnectionError:
        print('Error during download.')
        return ''
    
    
    