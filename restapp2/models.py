from django.db import models
class product(models.Model):
    pid=models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=20)
# Create your models here.
