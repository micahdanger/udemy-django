from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    # this relates to the urls.py file: path(..., name='detail')
    def get_absolute_url(self):
        return reverse("basic_app:detail",kwargs={'pk':self.pk})

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    """
    related_name allows you to access the students of a school in the html template like this:

      {% for student in school_detail.students.all %}
        <p>{{student.name}} who is {{student.age}} years old.</p>
      {% endfor %}

    """
    school = models.ForeignKey(School,related_name='students')

    def __str__(self):
        return self.name
