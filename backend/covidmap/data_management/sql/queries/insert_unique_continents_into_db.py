import mysql.connector
from covidmap.data_management.functions.create_continent_relations import create_continent_relations

import environ
env = environ.Env()
environ.Env.read_env()

HOST = env('HOST')
USER = env('USER')
PASSWORD = env('PASSWORD')


def insert_unique_continents_into_db():
    df = create_continent_relations()

    try:
        mydb = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD
        )

        cursor = mydb.cursor()
        cursor.execute("CREATE SCHEMA IF NOT EXISTS `covid_data`")
        cursor.execute('USE `covid_data`')

        # cursor.execute("""
        #     CREATE TABLE IF NOT EXISTS `covidmap_continent` (
        #         id INT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
        #         continent VARCHAR(16) NOT NULL,
        #         PRIMARY KEY(id)
        #     );
        # """)

        query = """
            INSERT INTO covidmap_continent (continent)
                SELECT %s
                WHERE NOT EXISTS (SELECT 1 FROM covidmap_continent WHERE continent=%s);
        """

        for (idx, row) in df.iterrows():
            cursor.execute(query, (row.loc['continent'], row.loc['continent']))

        mydb.commit()
        
        return {"success": True, "error": ""}

    except mysql.connector.Error as e:
        print(e)
        return {"success": False, "error": e}


if __name__ == "__main__":
    insert_unique_continents_into_db()
