from django.db import models

# Create your models here.
class Hospice(models.Model):
 name = models.CharField(max_length=30)
 address = models.CharField(max_length=50)
 city = models.CharField(max_length=60)
 estdt = models.DateField()
 website = models.URLField()
 def __str__(self):
            return self.name

class Patient(models.Model):
 name = models.CharField(max_length=10)
 age = models.IntegerField()
 disease = models.CharField(max_length=60)
 pno= models.CharField(max_length=60) 
 def __str__(self):
            return self.name
 

class Admit(models.Model):
    hsp = models.ForeignKey(Hospice, on_delete=models.CASCADE)
    pname = models.ForeignKey(Patient, on_delete=models.CASCADE)
    admit_date = models.DateField()