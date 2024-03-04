from django.shortcuts import render

from app.models import Lesson, Student

def get_students(req):
  students = Student.objects
  if params := req.GET.get("contains"):
    students = students.get_only(params).get_ordered_by_name().all()
  else:
    students = students.get_ordered_by_name().all()
  return render(req, "index.html", {"iterable": students, "header": "Students"})

def get_lessons(req):
  lessons = Lesson.objects
  if teacher_name := req.GET.get("teacher"):
    lessons = lessons.get_today_lessons_by_teacher(teacher_name)
  else:
    lessons = lessons.all()
  return render(req, "lessons.html", {"lessons": lessons})