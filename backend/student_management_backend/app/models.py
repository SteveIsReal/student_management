from django.db import models
from datetime import datetime


class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name}, age : {self.age}"

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    mail = models.EmailField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"

class Course(models.Model):
    DAY = {
        "SUN" : "Sunday",
        "MON" : "Monday",
        "TUE" : "Tuesday",
        "WED" : "Wednesday",
        "THU" : "Thrusday",
        "FRI" : "Friday",
        "SAT" : "Saturday"
    }

    course_name = models.CharField(max_length=255)
    course_description = models.TextField()
    course_day = models.CharField(max_length=3, choices=DAY)
    course_start_time = models.TimeField()
    course_end_time = models.TimeField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return f"{self.course_name}, {self.course_day}: {self.course_start_time}-{self.course_end_time}"

class EnrollCourse(models.Model):
    date = models.DateField(default=datetime.now())
    enroll_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    present_student = models.ManyToManyField(Student, limit_choices_to={}, related_name="present_student")

    def __str__(self):
        return f"{self.enroll_course} / date : {self.date}"

class EnrollStudent(models.Model):
    enrolled_course = models.ForeignKey(EnrollCourse, on_delete=models.CASCADE)
    student_descripton = models.TextField()

    def __str__(self):
        return f"{self.student_descripton}"