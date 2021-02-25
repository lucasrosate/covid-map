import os
import pandas as pd


def create_location_relations():
    """
    Returns a table with unique locations and its IDs
    """
    
    file_path = os.path.join(os.path.dirname(__file__), '..', 'csv/owid-covid-data.csv')
    df = pd.read_csv(file_path)

    location_table = df.loc[:, ['location', 'date']]
    location_table.sort_values(by=['date'])
    location_table = location_table.drop(columns=['date'])
    location_table = location_table.drop_duplicates(subset=['location'])

    # location_table.to_csv('location_relations.csv', index=False)
    return location_table


if __name__ == "__main__":
    print(create_location_relations())
    