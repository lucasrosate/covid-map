#import sys
from django.apps import AppConfig
#from covidmap.data_management.sql.queries.insert_covid_data_into_db import insert_covid_data_into_db


class CovidmapConfig(AppConfig):
    name = 'covidmap'
    
    def ready(self):
        """
        This function is supposed to be called everytime server is started
        ---------------------------------------------------------------------------------------------------------
        insert_unique_continents_into_db: Function that inserts all distinct continents from the covid_data table
        
        insert_unique_locations_into_db: Function that inserts all distinct locations from the covid_data table
        
        insert_covid_data_into_db: insert latest data from covid into db
        """
        
        # if 'runserver' in sys.argv:
        #     print('Running fetch data functions...')
        #     insert_covid_data_into_db()
        #     print('Getting most recent covid data and inserting into table...')
            
        #     print('All done!')
            
            
        
