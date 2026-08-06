from django import forms
from .models import Book, Student, Address, Department, Course, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address', 'card', 'department', 'courses']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city']

class ProfileForm(forms.ModelForm):  
    class Meta:
        model = Profile
        fields = ['name', 'picture']

