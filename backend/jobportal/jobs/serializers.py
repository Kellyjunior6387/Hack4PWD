# jobs/serializers.py
from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    employer_name = serializers.CharField(source='employer.name')# Fetch employer's name
    class Meta:
        model = Job
        fields = ['employer_name', 'status', 'title', 'type']  # Limit the fields in the responseDe


class JobDetailSerializer(serializers.ModelSerializer):
    employer_name = serializers.CharField(source='employer.name')# Fetch employer's name
    class Meta:
        model = Job
        fields = ['title', 'employer_name', 'status', 'description_id', 'type']
