from django.urls import path

from app.views import form_submit, get_customers, index

urlpatterns = [
  path('', index, name='index'),
  path('customers/', get_customers, name='customers_view'),
  path('customer-form/', form_submit, name='form_view'),
]