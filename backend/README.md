<!--# 
data_route=YOUR_SERVER_URL/covidmap/get_todays_data
 $-->
# Backend

The backend was made in django-rest-framework. The main task of this it's to fetch all processed data from DB and send it to front-end.

The server is configured to use MySQL server, you can change by configuring in ```settings.py```, but things might not work correctly, since the crawler queries was made for this db in specific.

### Localrun
It's highly recommended to install a virtual enviroment before anything. You can check this tutorial [here](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/).


Steps:
1. Run ``` pip install requirements.txt``` to install all requirements;
2. Create a ```.env``` file in your project folder (```backend/backend```);
3. Put your MySQL server config
```
NAME=<your-db-schema-name>
USER=<user-db>
PASSWORD=<your-password> (You must use a SHA encrypted password)
HOST=<host>
PORT=<port>
```

4. Create another .env in ```covidmap/data-management/sql/queries``` and fill with the same content.
5. Type ``python manage.py makemigrations covidmap``
6. Type ```python manage.py update_covid_data``` to run the crawler, the processed data will be saved in ```covidmap/data-management/csv/owid-covid-data.csv``` (this data is provided by <em>Our World in Data</em>, you can check [here](https://ourworldindata.org/coronavirus-source-data)).
7. Then ```python manage.py runserver```.
8. Data from api can be get by send a request to ```{{data_route}}```.