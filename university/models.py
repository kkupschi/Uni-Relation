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