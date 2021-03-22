import logging
from django.core.management.base import CommandError
from covidmap.data_management.sql.queries.insert_covid_data_into_db import insert_covid_data_into_db
from covidmap.data_management.sql.queries.insert_unique_continents_into_db import insert_unique_continents_into_db
from covidmap.data_management.sql.queries.insert_unique_locations_into_db import insert_unique_locations_into_db
from covidmap.data_management.sql.queries.insert_most_recent_data import insert_most_recent_data


logger = logging.getLogger(__name__)


def get_new_data() -> bool:
    try:
        logger.info('Running fetch data functions...')
        
        insert_covid_data_into_db()
        logger.info('Getting most recent covid data and inserting into table...')
    
        insert_unique_continents_into_db()
        logger.info('Inserting table with distinct continents...')
        
        insert_unique_locations_into_db()
        logger.info('Inserting table with distinct locations...')
        
        insert_most_recent_data()
        logger.info('Creating table with most recent data...')
        
        logger.info('All done!')
        
        return True
    
    except UnicodeDecodeError as u_error:
        raise CommandError("Fetch data failed. {}".format(u_error)) 
        return False
        