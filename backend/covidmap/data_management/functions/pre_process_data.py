import os
import pandas as pd
from covidmap.data_management.functions.download_covid_csv import download_covid_csv


def pre_process_data(most_recent=True) -> None:
    """
    Select only important informations to show .
    
    Parameter
    ----------------------------------------------
    most_recent: bool
    If it is true it will download the most recent covid data file
    """
    
    if most_recent:
        file_path = download_covid_csv()
        if file_path is None:
            raise IOError
    else:
        try:
            path = os.path.join(os.path.dirname(__file__), '..') 
            file_path = os.path.join(path, 'csv', 'owid-covid-data.csv')
        except IOError:
            raise IOError
        
    # save_path = os.path.join(path, 'csv/processed_data.csv')
    
    df = pd.read_csv(file_path)
    
    filtered_df = df.loc[:,
                            [
                            'continent',
                            'location',
                            'date',
                            
                            'new_cases_smoothed',
                            'new_deaths_smoothed',
                            'new_tests_smoothed',
                            'new_vaccinations_smoothed',
                            
                            'total_cases',
                            'total_deaths',
                            'total_tests',
                            'people_vaccinated',
                            'population_density',
                            'population',
                            #'aged_65_older',
                            #'aged_70_older',
                            #'extreme_poverty',
                            #'cardiovasc_death_rate',
                            #'diabetes_prevalence',
                            #'female_smokers',
                            #'male_smokers',
                            'life_expectancy',
                            'human_development_index'
                            ]
                        ]
    
    filtered_df = filtered_df.where((pd.notnull(filtered_df)), 0)
    filtered_df.iloc[:, 0] = filtered_df.iloc[:, 0].fillna('other')

    filtered_df.insert(0, 'continent_id', pd.factorize(filtered_df['continent'])[0] + 1)
    filtered_df.insert(1, 'location_id', pd.factorize(filtered_df['location'])[0] + 1)

    filtered_df = filtered_df.drop(columns=['continent', 'location'])
    
    filtered_df.sort_values(by=['date', 'location_id'], ascending=True)
    
    filtered_df.loc[:, 'new_cases_smoothed':'life_expectancy'] = filtered_df.loc[:, 'new_cases_smoothed':'life_expectancy'].astype('int64')
    
    # filtered_df.to_csv(save_path, index=False)
    
    return filtered_df


if __name__ == "__main__":
    print(pre_process_data())
