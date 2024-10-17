# jobs/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Job
from rest_framework import status
from .serializers import JobSerializer, JobDetailSerializer, JobCreateSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

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
    # Remove authentication requirement for now
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = JobCreateSerializer(data=request.data)

        if serializer.is_valid():
            job = serializer.save()  # This will call the create method in JobCreateSerializer
            return Response(JobCreateSerializer(job).data, status=status.HTTP_201_CREATED)
        
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
            # Build a query to check if any tag in tag_query is in accessibility_tags
            tag_filters = Q()
            for tag in tag_query:
                tag_filters |= Q(accessibility_tags__icontains=tag)
            jobs = jobs.filter(tag_filters)

        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

