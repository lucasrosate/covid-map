import mysql.connector
from covidmap.data_management.functions.create_location_relations import create_location_relations

import environ
env = environ.Env()
environ.Env.read_env()

HOST = env('HOST')
USER = env('USER')
PASSWORD = env('PASSWORD')


def insert_unique_locations_into_db():
    df = create_location_relations()
    
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
        #     CREATE TABLE IF NOT EXISTS `covidmap_location` (
        #         id INT(8) UNSIGNED NOT NULL AUTO_INCREMENT,
        #         location VARCHAR(32) NOT NULL,
        #         PRIMARY KEY(id)
        #     );
        # """)
        
        query = """
            INSERT INTO covidmap_location (location)
                SELECT %s
                WHERE NOT EXISTS (SELECT 1 FROM covidmap_location WHERE location=%s);
        """
        
        for (idx, row) in df.iterrows():
            cursor.execute(query, (row.loc['location'], row.loc['location']))
                
        mydb.commit()
                
        return {"success": True, "error": ""}
    
    except mysql.connector.Error as e:
        print(e)
        return {"success": False, "error": e}
    

if __name__ == "__main__":
    insert_unique_locations_into_db()
    