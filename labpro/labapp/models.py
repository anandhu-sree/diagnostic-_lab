from django.db import models

# Create your models here.
class regmodel(models.Model):
    fullname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    email=models.EmailField()
    gender=models.CharField(max_length=20)
    phone=models.IntegerField()
    password=models.CharField(max_length=30)

class userregmodel(models.Model):
    fullname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    email=models.EmailField()
    gender=models.CharField(max_length=20)
    phone=models.IntegerField()
    password=models.CharField(max_length=30)

class apoint(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    date=models.DateField()
    time=models.CharField(max_length=200)
    department=models.CharField(max_length=50)
    price=models.IntegerField()

# #
class paymentmodel(models.Model):
    cardnumber=models.IntegerField()
    cvv=models.IntegerField()
    email_id=models.EmailField()
    exp_date=models.DateField()
    amount=models.IntegerField()


class services_model(models.Model):
    testname=models.CharField(max_length=25)
    test_desc= models.CharField(max_length=100)
    test_price = models.IntegerField()
    test_image=models.FileField(upload_to='labapp/static/')

