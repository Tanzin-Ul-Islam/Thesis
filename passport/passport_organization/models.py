from django.db import models

# Create your models here.
class passport_model(models.Model):
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    father_name= models.CharField(max_length=100)
    mother_name= models.CharField(max_length=100)
    dob= models.DateField()
    address= models.CharField(max_length=200)
    finger_print= models.CharField(max_length=100)
    blood_group= models.CharField(max_length=5)
    gender= models.CharField(max_length=10)
