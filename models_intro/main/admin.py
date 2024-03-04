from django.contrib import admin

from main.models import Country, Citizen, City

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Citizen)