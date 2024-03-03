from django.urls import path

from app.views import get_lessons, get_students

urlpatterns = [
  path('students/', get_students),
  path('lessons/', get_lessons),
]