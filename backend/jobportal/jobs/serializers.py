# jobs/serializers.py
from rest_framework import serializers
from .models import Job, AccessibilityTag

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

class JobCreateSerializer(serializers.ModelSerializer):
    accessibility_tags = serializers.ListField(
        child=serializers.ChoiceField(choices=AccessibilityTag.TAG_CHOICES),
        write_only=True
    )
    
    class Meta:
        model = Job
        fields = ['title', 'description_id', 'type', 'status', 'accessibility_tags']

    def create(self, validated_data):
        accessibility_tags = validated_data.pop('accessibility_tags')
        job = Job.objects.create(**validated_data)
        # Create accessibility tags associated with the job
        for tag in accessibility_tags:
            AccessibilityTag.objects.create(job=job, tag=tag)
        return job