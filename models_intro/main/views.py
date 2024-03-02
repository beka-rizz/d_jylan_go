from django.shortcuts import render

from main.models import Citizen, City, Country

def get_country_by_name(request):
  countries = Country.objects
  if _name := request.GET.get('name'):
    countries = countries.filter(name=_name.capitalize())

  countries = countries.all()
  return render(request, "index.html", {"iterable": countries, "header": "Countries"})

def get_cities(request):
  cities = City.objects
  if _country_id := request.GET.get('country_id'):
    cities = cities.filter(country_id=_country_id.capitalize()).all()
  
  cities = cities.all()
  return render(request, "index.html", {"iterable": cities, "header": "Cities"})

def get_citizens(request):
  citizens = Citizen.objects
  
  if country_name := request.GET.get("country_name"):
    citizens = citizens.filter(country__name__iexact=country_name)
    
  if request.GET.get("is_criminal") is not None:
    citizens = citizens.criminals()
  else:
    citizens = citizens.not_criminals()
  
  citizens = citizens.all()
  
  return render(request, "index.html", {"iterable": citizens, "header": "Citizens"})