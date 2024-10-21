# jobs/serializers.py
from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.ModelSerializer):
    employer_name = serializers.CharField(source='employer.username')  # Fetch employer's name
   

    class Meta:
        model = Job
        fields = ['id','employer_name', 'status', 'title', 'type','accessibility_tags']



class JobDetailSerializer(serializers.ModelSerializer):
    employer_name = serializers.CharField(source='employer.username')# Fetch employer's name
    class Meta:
        model = Job
        fields = ['title', 'employer_name', 'status', 'description_id', 'type', 'accessibility_tags']

class JobCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Job
        fields = ['title', 'description_id', 'type', 'status','accessibility_tags']

    def create(self, validated_data):
        employer = self.context['request'].user
        job = Job.objects.create(employer=employer, **validated_data)
        # Create accessibility tags associated with the job
        return job
