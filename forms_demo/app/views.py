from django.shortcuts import render

from app.models import Customer
from .forms import CustomerForm

def index(request):
  context = {}
  return render(request, "index.html", context)

def get_customers(request):
  customers = Customer.objects.all()
  context = {'customers': customers}
  return render(request, "customers.html", context)

def form_submit(request):
  form = CustomerForm()
  
  if request.method == "POST":
    print(request.POST)
    form = CustomerForm(request.POST)
    if form.is_valid():
      form.save()

  context = {'form': form}
  return render(request, "form.html", context)