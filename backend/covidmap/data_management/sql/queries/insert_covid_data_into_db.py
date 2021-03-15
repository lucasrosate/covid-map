import mysql.connector
from datetime import datetime
from covidmap.data_management.functions.pre_process_data import pre_process_data

import environ
env = environ.Env()
environ.Env.read_env()

NAME = env('NAME')
HOST = env('HOST')
USER = env('USER')
PASSWORD = env('PASSWORD')


def insert_covid_data_into_db():
    df = pre_process_data()
    try:
        mydb = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD
        )

        cursor = mydb.cursor()
        cursor.execute("CREATE SCHEMA IF NOT EXISTS " + NAME)
        cursor.execute('USE ' + NAME)

        query = """
            INSERT INTO covidmap_coviddata (
                continent_id,
                location_id,
                date_registered, 
                new_cases_smoothed, 
                new_deaths_smoothed,
                new_tests_smoothed, 
                new_vaccinations_smoothed,
                total_cases, 
                total_deaths, 
                total_tests, 
                people_vaccinated,
                population_density, 
                population, 
                life_expectancy, 
                human_development_index,
                time_picked
                )
                SELECT %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                WHERE NOT EXISTS (
                    SELECT id, date_registered, location_id FROM covidmap_coviddata
                    WHERE date_registered=%s AND location_id=%s
                    );
        """

        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print(now)

        for (_, row) in df.iterrows():
            data = (
                row.loc['continent_id'],
                row.loc['location_id'],
                row.loc['date'],
                row.loc['new_cases_smoothed'],
                row.loc['new_deaths_smoothed'],
                row.loc['new_tests_smoothed'],
                row.loc['new_vaccinations_smoothed'],
                row.loc['total_cases'],
                row.loc['total_deaths'],
                row.loc['total_tests'],
                row.loc['people_vaccinated'],
                row.loc['population_density'],
                row.loc['population'],
                row.loc['life_expectancy'],
                row.loc['human_development_index'],
                now,
                row.loc['date'],
                row.loc['location_id'],

            )

            cursor.execute(query, data)
        mydb.commit()

        return {"success": True, "error": ""}

    except mysql.connector.Error as e:
        print(e)
        return {"success": False, "error": e}


if __name__ == "__main__":
    insert_covid_data_into_db()
