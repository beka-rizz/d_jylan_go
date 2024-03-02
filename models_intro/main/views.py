from django.shortcuts import render

from main.models import City, Country

def get_country_by_name(request):
  if _name := request.GET.get('name'):
    print(_name.capitalize())
    countries = Country.objects.filter(name=_name.capitalize())
  else:
    countries = Country.objects.all()
  return render(request, "index.html", {"iterable": countries, "header": "Countries"})

def get_cities(request):
  if _country_id := request.GET.get('country_id'):
    cities = City.objects.filter(country_id=_country_id.capitalize())
  else:
    cities = City.objects.all()
  return render(request, "index.html", {"iterable": cities, "header": "Cities"})

def get_cities_by_country_name(request):
  if country_name := request.GET.get('country_name'):
    cities = City.objects.filter(country__name=country_name)
  else:
    cities = City.objects.all()
  return render(request, "index.html", {"iterable": cities, "header": "Cities"})
