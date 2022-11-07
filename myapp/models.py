from django.db import models

# Create your models here.
class UserMaster(models.Model):
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now=True)
    is_updated = models.DateTimeField(auto_now=True)
   

class Candidate(models.Model):
    user_id=models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    country =models.CharField(max_length=50,null =True)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    min_salary = models.BigIntegerField(null =True)
    max_salary = models.BigIntegerField(null =True)
    edu_level = models.CharField(max_length=50,null =True)
    experience = models.CharField(max_length=50,null =True)
    dob = models.CharField(max_length=50) 
    gender = models.CharField(max_length=50)
    jobdescription = models.CharField(max_length=150,null =True)
    job_type = models.CharField(max_length=50,null =True)
    job_category = models.CharField(max_length=50,null =True)
    profile_pic = models.ImageField(upload_to="app/img/candidate")
    
   
class Company(models.Model):
     user_id=models.ForeignKey(UserMaster,on_delete=models.CASCADE)
     company_name = models.CharField(max_length=150)
     state = models.CharField(max_length=50)
     city = models.CharField(max_length=50)
     contact = models.CharField(max_length=50)
     address = models.CharField(max_length=150)
     logo_pic = models.ImageField(upload_to="app/img/company")
    
     