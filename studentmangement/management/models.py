from django.db import models
from django.contrib.auth.models import User
class Student(models.Model):
    fk = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.TextField(max_length=50)
    age = models.IntegerField()
    contact = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name
    