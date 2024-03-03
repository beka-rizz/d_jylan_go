from django.urls import path

from app.views import get_students

urlpatterns = [
  path('students/', get_students),
]