from django.contrib import admin
from covidmap.models import Continent, Location, CovidData


# Register your models here.
class ContinentAdmin(admin.ModelAdmin):
    pass


class LocationAdmin(admin.ModelAdmin):
    pass


class CovidDataAdmin(admin.ModelAdmin):
    pass


admin.site.register(Continent, ContinentAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(CovidData, CovidDataAdmin)
