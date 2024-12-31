from django.contrib import admin
from .models import User , Complaint

# Register your models here.

# Register the Ldap model with the admin site
admin.site.register(User)
admin.site.register(Complaint)