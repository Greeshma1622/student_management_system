from django.contrib import admin
from .models import Departments,Contact
# Register your models here.

admin.site.register(Departments)

class Customerdetails(admin.ModelAdmin):
    list_display=('name','new_phno','email')
admin.site.register(Contact,Customerdetails)