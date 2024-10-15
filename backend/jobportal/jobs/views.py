# jobs/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Job
from rest_framework import status
from .serializers import JobSerializer, JobDetailSerializer
from django.shortcuts import get_object_or_404

class JobListAPIView(APIView):
    def get(self, request):
        jobs = Job.objects.all()  # Fetch all Job 
        serializer = JobSerializer(jobs, many=True)  # Serialize all job entries
        return Response(serializer.data)  # Return serialized data as JSON response
    
class JobDetailAPIView(APIView):
    def get(self, request, job_id):
        # Use get_object_or_404 to fetch the job or return a 404 if not found
        job = get_object_or_404(Job, id=job_id)
        serializer = JobDetailSerializer(job)  # Serialize the job instance
        return Response(serializer.data, status=status.HTTP_200_OK)
        
