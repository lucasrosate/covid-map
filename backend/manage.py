#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from covidmap.data_management.sql.queries.insert_covid_data_into_db import insert_covid_data_into_db
from covidmap.data_management.sql.queries.insert_unique_continents_into_db import insert_unique_continents_into_db
from covidmap.data_management.sql.queries.insert_unique_locations_into_db import insert_unique_locations_into_db


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    try:
        from django.core.management import execute_from_command_line
        
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    if 'update_covid_data' in sys.argv:
        print('Running fetch data functions...')
        
        insert_unique_continents_into_db()
        print('Inserting table with distinct continents...')
        
        insert_unique_locations_into_db()
        print('Inserting table with distinct locations...')
        
        insert_covid_data_into_db()
        print('Getting most recent covid data and inserting into table...')
        
        print('All done!')
    else:
        execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
