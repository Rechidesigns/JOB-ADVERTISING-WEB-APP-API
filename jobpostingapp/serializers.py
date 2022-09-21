from dataclasses import field
from rest_framework import serializers
from .models import Job_advert, Job_application

class Job_advertSerializer(serializers.ModelSerializer):
    job_application_count = serializers.ReadOnlyField()
    
    class Meta:
        model = Job_advert
        fields = '__all__'


class Job_applicationSerializer(serializers.ModelSerializer):
    job_advert_detail = serializers.ReadOnlyField()
    
    class Meta:
        model = Job_application
        fields = '__all__'