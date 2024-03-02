from django.urls import path

from main.views import get_cities, get_cities_by_country_name, get_country_by_name

urlpatterns = [
  path('countries/', get_country_by_name),
  path('cities/', get_cities),
  path('cities_by_country_name/', get_cities_by_country_name),
]
