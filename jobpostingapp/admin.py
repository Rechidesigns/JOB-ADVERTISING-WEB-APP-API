from django.contrib import admin
from .models import Job_advert, Job_application

admin.site.register([Job_advert, Job_application])
