from django.contrib import admin
from .models import StudentData

class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_roll','student_fname','student_lname','student_class','student_section','telugu','hindi','english','maths','science','social']

admin.site.register(StudentData,StudentAdmin)