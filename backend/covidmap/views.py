# # from django.contrib.auth.models import User, Group
# from rest_framework import viewsets
# # from rest_framework import permissions

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from covidmap.serializers import CovidGeneralDataSerializer
from covidmap.utils import get_most_recent_data, timer


class GetTodayCasesView(APIView):
    """
    View to return to user today's covid_data
    
    * Requires date today
    * Anyone can access this view
    """
    @timer
    def get(self, request, format=None):
        """
        Return covid data base on the date today
        """
        
        covid_data_today = get_most_recent_data()

        # covid_data_today = CovidData.objects.filter(
        #     date_registered=(datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        #     )
        
        if not covid_data_today:
            return Response(data={}, status=status.HTTP_204_NO_CONTENT)
        
        data_world = {}
        data_countries = []
        data_continents = []
        
        for cdt in covid_data_today:
            if cdt.continent_name == 'other':
                
                if cdt.location_name == 'World':
                    data_world = CovidGeneralDataSerializer(cdt).data
                elif cdt.location_name != "International":
                    data_continents.append(CovidGeneralDataSerializer(cdt).data)   
            else:
                data_countries.append(CovidGeneralDataSerializer(cdt).data)
        
        data = {
            "data_world": data_world,
            "data_cases_continents": data_continents,
            "data_cases_countries": data_countries
            }
        
        return Response(data=data, status=status.HTTP_200_OK)
    