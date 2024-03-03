from django.shortcuts import render

from app.models import Student

def get_students(req):
  students = Student.objects
  if params := req.GET.get("contains"):
    students = students.get_only(params).get_ordered_by_name().all()
  else:
    students = students.get_ordered_by_name().all()
  return render(req, "index.html", {"iterable": students, "header": "Students"})