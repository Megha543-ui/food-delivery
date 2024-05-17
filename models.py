from django.db import models

# Create your models here.
class SignupUser(models.Model):
    username= models.CharField(max_length=35, unique=True)
    email =models.CharField(max_length=60)
    phonenumber=models.CharField(max_length=10)
    Address=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    reenterpassword=models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Payment(models.Model):
    Fullname= models.CharField(max_length=35, unique=True)
    Email =models.CharField(max_length=60)
    Address=models.CharField(max_length=60)
    City=models.CharField(max_length=10)
    Zipcode=models.CharField(max_length=20)
    Cardnumber=models.CharField(max_length=20)
    Expmonth=models.CharField(max_length=20)
    Cvv=models.CharField(max_length=20)

    def __str__(self):
        return self.Fullname


class Contact(models.Model):
    myQuery= models.CharField(max_length=35)
    myName=models.CharField(max_length=60)
    myEmail=models.CharField(max_length=60)
    myPhone=models.CharField(max_length=10)
    eligible=models.CharField(max_length=20)
    mesg=models.CharField(max_length=20)

    def __str__(self):
        return self.myName
    
