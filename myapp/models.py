from django.db import models

# Create your models here.
class signup_master(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=12)
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    zipcode=models.IntegerField()

class adduser(models.Model):
        created=models.DateTimeField(auto_now_add=True)
        name=models.CharField(max_length=200)
        email=models.EmailField()
        #CHOICES = [('M','Male'),('F','Female')]
        #gender=models.CharField( max_length=20,choices=CHOICES)
        gender=models.CharField(max_length=20)
        subject=models.CharField(max_length=255,null=True,blank=True)
        city=models.CharField(max_length=20)
        address=models.TextField()