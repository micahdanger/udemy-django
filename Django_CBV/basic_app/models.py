from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principle = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basic_app:detail",kwargs={'pk':self.pk})

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    # EACH STUDENT HAS ONE SCHOOL, SIMILAR TO ITEMS HAVING A CHANNEL
    # RELATED_NAME WILL ALLOW US TO CALL THis lATER ON
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# NEXT REGISTER THESE IN THE admin.py FILE
