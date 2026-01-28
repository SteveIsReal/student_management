from django.contrib import admin
from .models import *


@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    pass

@admin.register(Teacher)
class AdminTeacher(admin.ModelAdmin):
    pass

@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    pass

@admin.register(EnrollCourse)
class AdminEnrollCourse(admin.ModelAdmin):
    pass

@admin.register(EnrollStudent)
class AdminEnrollStudent(admin.ModelAdmin):
    pass
