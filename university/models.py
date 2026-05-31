from django.db import models


class Semester(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Professor(models.Model):
    name = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class StudentCard(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=50)

    def __str__(self):
        return self.card_number


class Course(models.Model):
    title = models.CharField(max_length=200)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.title


class CourseDescription(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"Description: {self.course}"