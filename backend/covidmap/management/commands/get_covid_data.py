from django.core.management.base import BaseCommand, CommandError
from covidmap.data_management.functions.get_new_data import get_new_data

class Command(BaseCommand):
    help = "Forces the App to fetch new data from COVID World Map."

    def handle(self, *args, **options):
        try:
            get_new_data()
        except:
            raise CommandError("Fetch data failed.") 
        
        self.stdout.write(self.style.SUCCESS("Data fetched."))