import logging
from covidmap.data_management.sql.queries.insert_covid_data_into_db import insert_covid_data_into_db
from covidmap.data_management.sql.queries.insert_unique_continents_into_db import insert_unique_continents_into_db
from covidmap.data_management.sql.queries.insert_unique_locations_into_db import insert_unique_locations_into_db

logger = logging.getLogger(__name__)


def get_new_data():
    logger.info('Running fetch data functions...')
    
    insert_unique_continents_into_db()
    logger.info('Inserting table with distinct continents...')
    
    insert_unique_locations_into_db()
    logger.info('Inserting table with distinct locations...')
    
    insert_covid_data_into_db()
    logger.info('Getting most recent covid data and inserting into table...')
    
    logger.info('All done!') 
    