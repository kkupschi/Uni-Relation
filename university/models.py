from django.db import models


class Semester(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Professor(models.Model):
    name = models.CharField(max_length=100)
    fachgebiet = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Studentenausweis(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    ausweis_nr = models.CharField(max_length=50)

    def __str__(self):
        return self.ausweis_nr

class Kurs(models.Model):
    titel = models.CharField(max_length=200)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    studenten = models.ManyToManyField(Student)

    def __str__(self):
        return self.titel

class Kursbeschreibung(models.Model):
    kurs = models.OneToOneField(Kurs, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Beschreibung: {self.kurs}"