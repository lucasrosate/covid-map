import mysql.connector

import environ
env = environ.Env()
environ.Env.read_env()

NAME = env('NAME')
HOST = env('HOST')
USER = env('USER')
PASSWORD = env('PASSWORD')


def insert_most_recent_data():
    
    try:
        mydb = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD
        )

        cursor = mydb.cursor()
        cursor.execute('USE ' + NAME + ';')
        cursor.execute('DROP TABLE IF EXISTS covidmap_most_recent_cases;')
        cursor.execute("""CREATE TABLE IF NOT EXISTS covidmap_most_recent_cases(
                            id                          int NOT NULL AUTO_INCREMENT,
                            date_registered             date NOT NULL, 
                            new_cases_smoothed          int NOT NULL, 
                            new_deaths_smoothed         int NOT NULL,
                            new_tests_smoothed          int NOT NULL, 
                            new_vaccinations_smoothed   int NOT NULL,
                            total_cases                 bigint UNSIGNED NOT NULL, 
                            total_deaths                bigint UNSIGNED NOT NULL, 
                            total_tests                 int UNSIGNED NOT NULL, 
                            people_vaccinated           bigint NOT NULL,
                            population_density          double NOT NULL, 
                            population                  bigint NOT NULL, 
                            life_expectancy             double NOT NULL, 
                            human_development_index     double NOT NULL,
                            time_picked                 datetime NOT NULL,
                            continent_id                int NOT NULL,
                            location_id                 int NOT NULL,
                            PRIMARY KEY(id)
            );""")
        
        mydb.commit()
        
        cursor.execute("SELECT * FROM covid_data.covidmap_location;")
        all_location_ids = cursor.fetchall()
        
        for location in all_location_ids:
            cursor.execute(
                """
                    SELECT * FROM covid_data.covidmap_coviddata
                        WHERE location_id={}
                        ORDER BY date_registered DESC
                    LIMIT 1;
                """.format(location[0]))
            
            most_recent_data = cursor.fetchone()
            
            cursor.execute("""
            INSERT INTO covidmap_most_recent_cases (
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
                time_picked,
                continent_id,
                location_id
                )
                SELECT %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            """, (most_recent_data[1],
                    most_recent_data[2],
                    most_recent_data[3],
                    most_recent_data[4],
                    most_recent_data[5],
                    most_recent_data[6],
                    most_recent_data[7],
                    most_recent_data[8],
                    most_recent_data[9],
                    most_recent_data[10],
                    most_recent_data[11],
                    most_recent_data[12],
                    most_recent_data[13],
                    most_recent_data[14],
                    most_recent_data[15],
                    most_recent_data[16],
        ))
            
        mydb.commit()
            
        return {"success": True, "error": ""}

    except mysql.connector.Error as e:
        print(e)
        return {"success": False, "error": e}


if __name__ == "__main__":
    insert_most_recent_data()
    