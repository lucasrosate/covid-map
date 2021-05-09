import time
from datetime import datetime
from covidmap.models import CovidData


def get_most_recent_data():
    print("[{}] Data requested.".format(datetime.now().strftime("%d-%m-%Y")))
    return CovidData.objects.raw("SELECT * FROM covid_data.covidmap_most_recent_cases;")


def timer(func):
    """helper function to estimate view execution time"""
    
    def wrapper(*args, **kwargs):
        # record start time
        start = time.time()

        # func execution
        result = func(*args, **kwargs)
        
        duration = (time.time() - start) * 1000
        # output execution time to console
        print('view {} takes {:.2f} ms'.format(
            func.__name__, 
            duration
            ))
        return result
    return wrapper
