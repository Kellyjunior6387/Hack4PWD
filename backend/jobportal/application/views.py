from django.shortcuts import render
from rest_framework import generics
from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer

class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class ApplicationList(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

