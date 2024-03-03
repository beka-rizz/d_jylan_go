from django.db import models

class User(models.Model):
  name = models.CharField(max_length=20)
  
  def __str__(self):
    return self.name
  
  def __repr__(self):
    return f"User(name: {self.name})"
  
  class Meta:
    abstract = True


class Teacher(User):
  years_of_experience = models.IntegerField()
  
  def __repr__(self):
    return f"Teacher(name: {self.name}, years of experience: {self.years_of_experience})"
  
class Lesson(models.Model):
  title = models.CharField(max_length=10)
  date = models.DateField()
  duration = models.IntegerField()
  description = models.TextField()
  teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='lessons')
  students = models.ManyToManyField('Student', related_name='lessons')
  
  def __str__(self):
    return f"{self.title} {self.teacher}"
  
  def __repr__(self):
    return f"Lesson(title: {self.title}, date: {self.date}, teacher: {self.teacher})"

class StudentQuerySet(models.QuerySet):
  
  def get_only(self, params) -> models.QuerySet:
    return self.filter(name__contains=params)
  
  def get_ordered_by_name(self) -> models.QuerySet:
    return self.order_by("name")
  
class Student(User):
  course = models.CharField(max_length=30)
  objects = StudentQuerySet.as_manager()
  
  def __repr__(self):
    return f"Student(name: {self.name}, course: {self.course})"