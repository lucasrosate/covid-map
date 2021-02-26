from django.db import models
from django.core.validators import MaxValueValidator


class Continent(models.Model):
    continent = models.TextField(verbose_name="Continent")
    
    
class Location(models.Model):
    location = models.TextField(verbose_name="Location")


class CovidData(models.Model):
    """
    en: General data, it has daily change. \n
    pt: Dados gerais, mutáveis diáriamente.
    """
    continent = models.ForeignKey(Continent, on_delete=models.RESTRICT)
    
    location = models.ForeignKey(Location, on_delete=models.RESTRICT)
    
    date_registered = models.DateField(verbose_name="Date Registered")
    
    new_cases_smoothed = models.IntegerField(verbose_name="New Cases",
                                             null=0,
                                             validators=[MaxValueValidator(2097151)]
                                             )
    new_deaths_smoothed = models.IntegerField(verbose_name="new Deaths",
                                              null=0,
                                              validators=[MaxValueValidator(2097151)]
                                              )
    new_tests_smoothed = models.IntegerField(verbose_name="New Tests",
                                             null=0,
                                             validators=[MaxValueValidator(2097151)]
                                             )
    new_vaccinations_smoothed = models.IntegerField(verbose_name="New Vaccinations",
                                                    null=0,
                                                    validators=[MaxValueValidator(2097151)]
                                                    )

    total_cases = models.PositiveIntegerField(verbose_name="Total Cases",
                                              null=0
                                              )
    
    total_deaths = models.PositiveIntegerField(verbose_name="Total Deaths",
                                               null=0
                                               )
    
    total_tests = models.PositiveIntegerField(verbose_name="Total Tests",
                                              null=0
                                              )
    
    people_vaccinated = models.BigIntegerField(verbose_name="People Vaccinated",
                                               null=0
                                            )
    
    population_density = models.BigIntegerField(verbose_name="Population Density",
                                                null=0
                                             )
    
    population = models.BigIntegerField(verbose_name="Total Fully Vacinated",
                                             null=0
                                             )
    
    life_expectancy = models.PositiveIntegerField(verbose_name="Life Expectancy",
                                                  null=0
                                                  )
    
    human_development_index = models.FloatField(verbose_name="Human Development Index (HDI)")
    
    time_picked = models.DateTimeField(verbose_name="Time Picked Data")
    
    @property
    def location_name(self):
        return self.location.location
    
    @property
    def continent_name(self):
        return self.continent.continent
    
    

    
