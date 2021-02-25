"""
API routes \n
API_URL/ => Get All Data from Today
"""
import covidmap.urls
from rest_framework import routers
from django.urls import path, include


router = routers.SimpleRouter()

urlpatterns = [
    path(r'covidmap/', include(covidmap.urls))
]
