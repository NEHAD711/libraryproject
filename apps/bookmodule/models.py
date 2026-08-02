from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, null=True, blank=True)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.title

class Address(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city

class Card(models.Model):
    card_number = models.IntegerField()

    def __str__(self):
        return str(self.card_number)

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.IntegerField()

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    card = models.OneToOneField(Card, on_delete=models.PROTECT, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    courses = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name