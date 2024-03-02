from django.db import models

# Country <-> Citizen (One <-> Many)
# Country <-> City (One <-> Many)

class Base(models.Model):
  name = models.CharField(max_length=20)
  
  def __str__(self):
    return self.name
  
  class Meta:
    abstract = True
    

class Country(Base):
  language = models.CharField(max_length=20)
  population = models.IntegerField()
  area = models.DecimalField(max_digits=20, decimal_places=2)
  
  def __str__(self):
    return self.name
  
class City(Base):
  country = models.ForeignKey(Country, on_delete=models.CASCADE)
  
  
  
class Citizen(Base):
  age = models.IntegerField()
  country = models.ForeignKey(Country, on_delete=models.CASCADE)