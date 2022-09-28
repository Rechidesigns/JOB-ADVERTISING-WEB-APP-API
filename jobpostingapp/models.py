from datetime import date
from email.policy import default
from random import choices
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import model_to_dict
from phonenumber_field.modelfields import PhoneNumberField

# from django.conf import settings
# from django.contrib.auth.models import User

# OPTION_1 = (
#     ('MIDLE LEVEL', 'MIDLE LEVEL'),
#     ('MIDLE LEVEL', 'MIDLE LEVEL'),
#     ('SENIOR', 'SENIOR'),
#     )
#  choices=OPTION_1, default=None, blank=True, null=True)


class Job_advert(models.Model):

    EMPLOYMENT_CHOICES = (("full-time", "Full Time"),
                        ("contract", "Contract"),
                        ("remote","Remote"),
                        ("part-time", "Part Time"),)
    
    EMPLOYMENT_LEVELS = ( ("entry-level","Entry level"), 
                         ("mid-level","Mid-level"), 
                         ("senior","Senior"))
    
    STATUS = (("unpublished","Unpublished"), 
              ("published","Published"))

    title = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    employment_type = models.CharField(max_length=250, choices=EMPLOYMENT_CHOICES)
    experience_level = models.CharField(max_length=250, choices=EMPLOYMENT_LEVELS)
    description = models.TextField()
    location = models.CharField(max_length=150)
    job_description = models.TextField()
    status = models.CharField(max_length=100, choices=STATUS, default= 'published')
    date_posted = models.DateField(auto_now_add=True)

    def _str_(self):
        return self.tittle


    
    @property
    def job_application_count(self):
        return self.Job_application.all().values().count()



class Job_application(models.Model):

        
    EXPERIENCE_LEVELS = (("0 - 1", "0 - 1"), 
                         ("1 - 2", "1 - 2"), 
                         ("3 - 4", "3 - 4"),
                         ("5 - 6", "5 - 6"), 
                         ("7 and above", "7 and above")
                        )

    job_advert = models.ForeignKey(Job_advert, related_name= "Job_application", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email_address = models.EmailField()
    phone_no = PhoneNumberField()
    linkedin_profile_url = models.URLField(null=True, blank=True)
    github_url = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    years_of_experience = models.CharField(max_length=50, choices=EXPERIENCE_LEVELS)
    upload_cv = models.FileField(upload_to='documents/%Y/%m/%d/', null=True)
    cover_letter = models.TextField(null=True, blank=True)
    time_and_date_applied = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.first_name

    # Job_application = models.Person.objects.get(id = 25)
    # phoneNumber = Job_application.phoneNumber.as_e164
    
    @property
    def job_advert_detail(self):

        return model_to_dict(self.job_advert, fields=['tittle'])
