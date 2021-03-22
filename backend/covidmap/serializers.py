from rest_framework import serializers


class CovidGeneralDataSerializer(serializers.Serializer):
    continent_name = serializers.CharField(read_only=True)
    location_name = serializers.CharField(read_only=True)
    date_registered = serializers.DateField(read_only=True, format="%d/%m/%Y")
    new_cases_smoothed = serializers.IntegerField(read_only=True)                  
    new_deaths_smoothed = serializers.IntegerField(read_only=True)   
    new_tests_smoothed = serializers.IntegerField(read_only=True)                                  
    new_vaccinations_smoothed = serializers.IntegerField(read_only=True)                                        
    total_cases = serializers.IntegerField(read_only=True) 
    total_deaths = serializers.IntegerField(read_only=True) 
    total_tests = serializers.IntegerField(read_only=True) 
    people_vaccinated = serializers.IntegerField(read_only=True) 
    population_density = serializers.IntegerField(read_only=True) 
    population = serializers.IntegerField(read_only=True) 
    life_expectancy = serializers.IntegerField(read_only=True) 
    human_development_index = serializers.FloatField(read_only=True) 
