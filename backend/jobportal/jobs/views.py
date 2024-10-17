# jobs/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Job
from rest_framework import status
from .serializers import JobSerializer, JobDetailSerializer, JobCreateSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

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

class JobCreateAPIView(APIView):
    #permission_classes = [IsAuthenticated]  # Restrict access to authenticated users only
    """"""
    def post(self, request):
        # Ensure the user is an employer
        #if request.user.role != 'employer':
        #  return Response({'error': 'Only employers can create jobs.'}, status=status.HTTP_403_FORBIDDEN)

        # Set employer field to the logged-in user
        serializer = JobCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(employer=request.user)  # Pass the employer field as the logged-in user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

class JobSearchAPIView(APIView):
    def get(self, request):
        title_query = request.query_params.get('title', None)
        tag_query = request.query_params.getlist('tags')  # Expecting a list of tags

        # Filter jobs based on title and accessibility tags
        jobs = Job.objects.all()

        if title_query:
            jobs = jobs.filter(title__icontains=title_query)  # Search for title (case insensitive)

        if tag_query:
            print(tag_query)
            jobs = jobs.filter(accessibility_tags__icontains=tag_query)  # Filter by accessibility tags

        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

