from django.contrib import admin

from app.models import Lesson, Student, Teacher

admin.site.register(Teacher)
admin.site.register(Lesson)
admin.site.register(Student)