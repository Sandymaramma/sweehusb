from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=225)
  lastname = models.CharField(max_length=225)
  phone = models.IntegerField()
  joined_date = models.DateField()(default=date.today)
