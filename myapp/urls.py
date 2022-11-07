from django.urls import path,include
from . import views
urlpatterns = [
   path("",views.index,name="index"),
   path("signup/",views.sign,name="sign"),
   path("register/",views.RegisterUser,name="register"),
   path("otp/",views.Otpverify,name="otp"),
   path("optconfirm/",views.OtpConfirm,name="otpconfirm"),
   path("loginpage/",views.Loginpage,name="loginpage"),
   path("loginuser/",views.Loginuser,name="loginuser"),
   path("profile/<int:pk>",views.ProfilePage,name="profile"),
   path("profileupdate/<int:pk>",views.ProfileUpdate,name="profileupdate")
]