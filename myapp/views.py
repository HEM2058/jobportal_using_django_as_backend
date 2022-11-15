from django.shortcuts import render,redirect
from .models import *
from random import randint
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
# def index(request):
#     return render(request,'index.html')
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
             newuser.is_active = False
             newuser.save()
             message = f"Hello {fname},Your otp for HMRJP account is \n {otp}"
             send_mail(
             "Welcome to HMRJP - Verify Your Email",
             message,
             settings.EMAIL_HOST_USER,
             [email],
             fail_silently = False
             )
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
             newuser.is_active = False
             newuser.save()
             message = f"Hello {fname} ,Your otp for HMRJP account is \n {otp}"
             send_mail(
             "Welcome to HMRJP - Verify Your Email",
             message,
             settings.EMAIL_HOST_USER,
             [email],
             fail_silently = False
             )
             return render(request,'otpverify.html',{'email':email}) 


def Otpverify(request):
    return render(request,'otpverify.html')

def OtpConfirm(request):
     email = request.POST.get('email')
     otp = int(request.POST.get('otp'))
     user = UserMaster.objects.get(email=email)
     if user:
       
        if user.otp==otp:
           user.is_active = True
           user.save()
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
        if user.password == password and user.is_active == True:
          can = Candidate.objects.get(user_id=user)
          request.session['id'] = user.id
          request.session['role'] = user.role
          request.session['firstname'] = can.firstname
          request.session['lastname'] = can.lastname
          request.session['email'] = user.email
          request.session['password'] = user.password
          return render(request,'index.html')
        
        else:
         if user.password != password:
            message = "Password doesnot match"
            return render(request,'login.html',{'msg':message})
         else:
            message = "Signup before login"
            user.delete()
            return render(request,'signup.html',{'msg':message})
      else:
            message = "Candidate doesnot exist"
            return render(request,'login.html',{'msg':message})

    else:
     if request.POST.get('role', 'default_value')=="Company":
      email = request.POST.get('email')
      password = request.POST.get('password')

      user = UserMaster.objects.get(email=email)
      if user:
        if user.password == password and user.is_active == True:
          company = Company.objects.get(user_id=user)
          request.session['id'] = user.id
          request.session['role'] = user.role
          request.session['firstname'] = company.firstname
          request.session['lastname'] = company.lastname
          request.session['email'] = user.email
          request.session['password'] = user.password
          return redirect('companypage')
        
        else:
         if user.password != password:
            message = "Password doesnot match"
            return render(request,'login.html',{'msg':message})
         else:
            message = "Signup before login"
            user.delete()
            return render(request,'signup.html',{'msg':message})
      else:
            message = "Company doesnot exist"
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
         can.min_salary= request.POST.get('min_salary')
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
         can.save()
         url = f'/profile/{pk}' #formatting url
         return redirect(url)
    
############### Company Side ###############

def CompanyPage(request):
    return render(request,'Company/index.html')

def CompanyProfilePage(request,pk):
        user = UserMaster.objects.get(pk=pk)
        company = Company.objects.get(user_id=user)
        return render(request,'Company/profile.html',{'user':user,'company':company})

def CompanyProfileUpdate(request,pk):
       user = UserMaster.objects.get(id=pk)
       if user.role == "Company":
        company = Company.objects.get(user_id=user)
        company.country = request.POST.get('country')
        company.city = request.POST.get('city')
        company.state = request.POST.get('state')
        company.address = request.POST.get('address')
        company.company_name = request.POST.get('company_name')
        company.contact = request.POST.get('contact')
        company.company_des = request.POST.get('company_des')
        company.logo_pic = request.POST.get('logo_pic')
        company.save()
        url = f'/companyprofile/{pk}' #formatting url
        return redirect(url)

def JobPost(request):
    return render(request,'Company/jobpost.html')

def JobPostSubmit(request):
    user = UserMaster.objects.get(id=request.session.get('id'))
    if user.role =="Company": 
       company = Company.objects.get(user_id=user)
       jobname = request.POST['jobname']
       companyname = request.POST['companyname']
       companyaddress = request.POST['companyaddress']
       jobdescription = request.POST['jobdescription']
       qualification = request.POST['qualification']
       responsibilities = request.POST['responsibilities']
       location = request.POST['location']
       companyemail = request.POST['companyemail']
       companycontact = request.POST.get('companycontact')
       salarypackage = request.POST['salarypackage']
       experience = request.POST['experience']
       logo_pic = request.FILES.get('logo_pic')

       post = JobDetails.objects.create(company_id=company,jobname=jobname,companyname=companyname,
       companyaddress=companyaddress,jobdescription=jobdescription,qualification=qualification,responsibilities=responsibilities,location=location,companyemail=companyemail,salarypackage=salarypackage,experience=experience,logo_pic=logo_pic,companycontact=companycontact
       )
       message="Job Successfully posted"
       return render(request,'Company/jobpost.html',{'msg':message})
  
def JobList(request):
    alljob = JobDetails.objects.all()
    return render(request,'Company/joblist.html',{'alljob':alljob})

    
def CandidateJobList(request):
    alljob = JobDetails.objects.all()
    return render(request,'job-list.html',{'alljob':alljob})


def CompanyLogout(request):
     del request.session['email']
     del request.session['password']
     return redirect('loginpage')
    

def ApplyJob(request,pk):
    user = UserMaster.objects.get(id=request.session.get('id'))
    if user:
     cand = Candidate.objects.get(user_id=user)
     Job = JobDetails.objects.get(pk=pk)
    return render(request,'apply.html',{'user':user,'can':cand,'job':Job})

def JobSave(request,pk):
    user = UserMaster.objects.get(id=request.session.get('id'))
    if user:
        cand = Candidate.objects.get(user_id=user)
        job = JobDetails.objects.get(pk=pk)
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        contact = request.POST.get('contact')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        address = request.POST.get('address')
        edu_level = request.POST.get('edu_level')
        experience = request.POST.get('experience')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        jobdescription = request.POST.get('jobdescription')
        resume = request.FILES.get('resume')

        apply = ApplyList.objects.create(candidate_id=cand,job_id=job,firstname=firstname,lastname=lastname,contact=contact,country=country,state=state,city=city,address=address,edu_level=edu_level,experience=experience,dob=dob,gender=gender,jobdescription=jobdescription,resume=resume)
        message = "Job Apply Successfully !"
        return render(request,'job-list.html',{'msg':message})
        
