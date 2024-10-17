# jobs/serializers.py
from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.ModelSerializer):
    employer_name = serializers.CharField(source='employer.name')  # Fetch employer's name
   

    class Meta:
        model = Job
        fields = ['id','employer_name', 'status', 'title', 'type','accessibility_tags']



class JobDetailSerializer(serializers.ModelSerializer):
    employer_name = serializers.CharField(source='employer.name')# Fetch employer's name
    class Meta:
        model = Job
        fields = ['title', 'employer_name', 'status', 'description_id', 'type', 'accessibility_tags']

class JobCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Job
        fields = ['title', 'description_id', 'type', 'status','accessibility_tags','employer']

    def create(self, validated_data):
        job = Job.objects.create(**validated_data)
        # Create accessibility tags associated with the job
        return job
