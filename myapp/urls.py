from django.urls import path,include
from . import views
urlpatterns = [
   path("",views.sign,name="signup"),
   path("register/",views.RegisterUser,name="register"),
   path("otp/",views.Otpverify,name="otp"),
   path("optconfirm/",views.OtpConfirm,name="otpconfirm"),
   path("Loginpage/",views.Loginpage,name="loginpage"),
   path("loginuser/",views.Loginuser,name="loginuser"),
   path("profile/<int:pk>",views.ProfilePage,name="profile"),
   path("profileupdate/<int:pk>",views.ProfileUpdate,name="profileupdate"),
   path("candidatejoblist/",views.CandidateJobList,name="candidatejoblist"),


    ############### Company Side ###############

   path("companypage/",views.CompanyPage,name="companypage"),
   path("companyprofile/<int:pk>",views.CompanyProfilePage,name="companyprofile"),
   path("companyprofileupdate/<int:pk>",views.CompanyProfileUpdate,name="companyprofileupdate"),
   path("companylogout",views.CompanyLogout,name="companylogout"),
    ############### Company Side:Job Post ###############
   path("jobpost/",views.JobPost,name="jobpost"),
   path("jobsubmit/",views.JobPostSubmit,name="jobsubmit"),
   path("joblist/",views.JobList,name="joblist")
 

]