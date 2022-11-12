from django.db import models

# Create your models here.
class UserMaster(models.Model):
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    time_st = models.DateTimeField(auto_now = True)
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
     firstname = models.CharField(max_length=50,null=True)
     lastname = models.CharField(max_length=50,null=True)
     company_name = models.CharField(max_length=150)
     country =models.CharField(max_length=50,null =True)
     state = models.CharField(max_length=50)
     city = models.CharField(max_length=50)
     contact = models.CharField(max_length=50)
     address = models.CharField(max_length=150)
     logo_pic = models.ImageField(upload_to="app/img/company")
     company_des = models.CharField(max_length=150, null=True)

class JobDetails(models.Model):
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE,null = True)
    jobname = models.CharField(max_length=250)
    companyname = models.CharField(max_length=250)
    jobdescription = models.CharField(max_length=250)
    qualification = models.CharField(max_length=250)
    responsibilities = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    companyemail = models.CharField(max_length=50)
    companycontact = models.CharField(max_length=50)
    salarypackage = models.CharField(max_length=50)
    experience = models.IntegerField()  
    companyaddress = models.CharField(max_length=50,null=True)
    logo_pic = models.ImageField(upload_to="app/img/company",null=True)