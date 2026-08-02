from django.contrib import admin
from .models import Book, Address, Card, Department, Course, Student

admin.site.register(Book)
admin.site.register(Address)
admin.site.register(Card)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Student)