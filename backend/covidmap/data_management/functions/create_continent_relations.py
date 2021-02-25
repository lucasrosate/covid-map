import os
import pandas as pd


def create_continent_relations():
    """
    Returns a table with unique continents and its IDs
    """
    file_path = os.path.join(os.path.dirname(__file__), '..', 'csv/owid-covid-data.csv')
    df = pd.read_csv(file_path)

    continent_table = df.loc[:, ['continent', 'date']]

    continent_table.sort_values(by=['date'])
    continent_table.iloc[:, 0] = continent_table.iloc[:, 0].fillna('other')
    continent_table = continent_table.drop(columns=['date'])
    continent_table = continent_table.drop_duplicates(subset=['continent'])

    # continent_table.to_csv('continent_table_relations.csv', index=False)
    return continent_table


if __name__ == "__main__":
    print(create_continent_relations())
    