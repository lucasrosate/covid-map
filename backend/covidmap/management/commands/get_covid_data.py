from django.core.management.base import BaseCommand
from covidmap.data_management.functions.get_new_data import get_new_data


class Command(BaseCommand):
    help = "Forces the App to fetch new data from COVID World Map."

    def handle(self, *args, **options):
        success: bool = get_new_data()
        
        if success:
            self.stdout.write(self.style.SUCCESS("Data fetched."))
            