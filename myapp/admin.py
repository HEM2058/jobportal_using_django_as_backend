from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserMaster)
admin.site.register(Candidate)
admin.site.register(Company)