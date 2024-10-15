# jobs/urls.py
from django.urls import path
from .views import JobListAPIView, JobDetailAPIView, JobSearchAPIView, JobCreateAPIView

urlpatterns = [
    path('' , JobListAPIView.as_view(), name='job-list-api'),
    path('<int:job_id>/', JobDetailAPIView.as_view(), name='job-detail-api'),  # Detail view
    path('create/', JobCreateAPIView.as_view(), name='job-create-api'),
    path('search/', JobSearchAPIView.as_view(), name='job-search-api'),
]
