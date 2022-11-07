from django.shortcuts import render,redirect
from .models import *
from random import randint

# Create your views here.
def index(request):
    return render(request,'index.html')
def sign(request):
    return render(request,'signup.html')

def RegisterUser(request):
    
    #Candidate Registration    
    if request.POST.get('role', 'default_value')=="Candidate":
        role = request.POST['role']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST.get('cpassword','default_value')

        user = UserMaster.objects.filter(email=email)
        if user:
            message="Candidate already exist"
            return render(request,'signup.html',{'msg':message})
        else:
            if password == cpassword:
             otp = randint(100000,999999)
             newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
             newcand = Candidate.objects.create(user_id=newuser,firstname=fname,lastname=lname) 
             return render(request,'otpverify.html',{'email':email})
    else:
        #Company Registration   
        role = request.POST['role']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST.get('cpassword','default_value')

        user = UserMaster.objects.filter(email=email)
        if user:
            message="Candidate already exist"
            return render(request,'signup.html',{'msg':message})
        else:
            if password == cpassword:
             otp = randint(100000,999999)
             newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
             newcand = Company.objects.create(user_id=newuser,firstname=fname,lastname=lname) 
             return render(request,'otpverify.html',{'email':email}) 


def Otpverify(request):
    return render(request,'otpverify.html')

def OtpConfirm(request):
     email = request.POST.get('email')
     otp = int(request.POST.get('otp'))
     user = UserMaster.objects.get(email=email)

     if user:
        if user.otp==otp:
           message = "Otp verify successfully"
           return render(request,'login.html',{'msg':message}) 
        else:
             message = "Otp is incorrect"
             return render(request,'otpverify.html',{'msg':message}) 
        
     else:
      return render(request,'signup.html')

def Loginpage(request):
    return render(request,'login.html')

def Loginuser(request):
    if request.POST.get('role', 'default_value')=="Candidate":
      email = request.POST.get('email')
      password = request.POST.get('password')

      user = UserMaster.objects.get(email=email)
      if user:
        if user.password == password and user.role == "Candidate":
          can = Candidate.objects.get(user_id=user)
          request.session['id'] = user.id
          request.session['role'] = user.role
          request.session['firstname'] = can.firstname
          request.session['lastname'] = can.lastname
          request.session['email'] = user.email
          return redirect('index')
        
        else:
            message = "Password doesnot match"
            return render(request,'login.html',{'msg':message})
      else:
            message = "User doesnot exist"
            return render(request,'login.html',{'msg':message})

def ProfilePage(request,pk):
        user = UserMaster.objects.get(pk=pk)
        can = Candidate.objects.get(user_id=user)
        return render(request,'profile.html',{'user':user,'can':can})

def ProfileUpdate(request,pk):
     user = UserMaster.objects.get(id=pk)
     if user.role == "Candidate":
         can = Candidate.objects.get(user_id=user) 
         can.country = request.POST.get('country')
         can.city = request.POST.get('city')
         can.state = request.POST.get('state')
         can.address = request.POST.get('address')
         can.min_salary= request.POST.get('country')
         can.max_salary = request.POST.get('max_salary')
         can.edu_level = request.POST.get('edu_level')
         can.experience = request.POST.get('experience')
         can.dob = request.POST.get('dob')
         can.gender = request.POST.get('gender')
         can.jobdescription = request.POST.get('jobdescription')
         can.job_type = request.POST.get('job_type')
         can.job_category = request.POST.get('job_category')
         can.contact = request.POST.get('contact')
         can.profile_pic = request.FILES.get('profile_pic')
         can.save(country=can.country)
         url = f'/profile/{pk}' #formatting url
         return redirect(url)
         
        

     