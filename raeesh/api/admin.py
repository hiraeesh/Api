from django.contrib import admin

# Register your models here.
from .models import Student

@admin.register(Student)
class StuAdmin(admin.ModelAdmin):
    list_display=['id','name','age','city','myimage']
