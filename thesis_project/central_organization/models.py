from django.db import models

# Create your models here.
class Central_model(models.Model):
    id = models.AutoField(primary_key=True)
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    father_name= models.CharField(max_length=100)
    mother_name= models.CharField(max_length=100)
    dob= models.DateField()
    address= models.CharField(max_length=200)
    finger_print= models.CharField(max_length=100)
    blood_group= models.CharField(max_length=5)
    gender= models.CharField(max_length=10)
    maritual_state= models.CharField(max_length=15)
    add_date = models.DateTimeField(auto_now_add=True)

