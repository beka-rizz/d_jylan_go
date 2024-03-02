from django.urls import path

from main.views import get_cities, get_citizens, get_country_by_name

urlpatterns = [
  path('countries/', get_country_by_name),
  path('cities/', get_cities),
  path('citizens/', get_citizens),
]
