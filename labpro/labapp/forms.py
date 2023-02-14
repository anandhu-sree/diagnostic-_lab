import datetime

from django import forms
from .models import *
class regform(forms.Form):
    fullname=forms.CharField(max_length=30)
    username=forms.CharField(max_length=30)
    email=forms.EmailField()
    phone=forms.IntegerField()
    gender=forms.CharField(max_length=20)
    password=forms.CharField(max_length=30)
    cpassword=forms.CharField(max_length=30)

class logform(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)

class userregform(forms.Form):
    fullname=forms.CharField(max_length=30)
    username=forms.CharField(max_length=30)
    email=forms.EmailField()
    phone=forms.IntegerField()
    gender=forms.CharField(max_length=20)
    password=forms.CharField(max_length=30)
    cpassword=forms.CharField(max_length=30)

class userlogform(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)
def present_or_future_date(value):
    if value<datetime.date.today():
        raise forms.ValidationError("error")
    return value
class apointform(forms.Form):
    name=forms.CharField(max_length=30)
    email=forms.EmailField()
    date=forms.DateField(validators=[present_or_future_date])
    time=forms.CharField(max_length=200)
    department=forms.CharField(max_length=50)
    price=forms.IntegerField()

class paymentform(forms.Form):
    cardnumber=forms.IntegerField()
    cvv=forms.IntegerField()
    email_id=forms.EmailField()
    exp_date=forms.DateField()
    amount=forms.IntegerField()


class addservices(forms.Form):
    testname=forms.CharField(max_length=25)
    test_desc= forms.CharField(max_length=100)
    test_price =forms.IntegerField()
    test_image=forms.FileField()
