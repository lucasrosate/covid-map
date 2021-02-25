
from django.urls import path

from covidmap.views import GetTodayCasesView

urlpatterns = [
    path(r'get-todays-data/', GetTodayCasesView.as_view(), name="get_todays_data")
]
