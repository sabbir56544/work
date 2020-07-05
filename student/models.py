from django.db import models


class StudentList(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField()
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    group = models.CharField(max_length=30)

    def __str__(self):
        return self.name
