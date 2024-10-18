from django.urls import path
from .views import ApplicationCreateView, ApplicationListView

urlpatterns = [
    path('applications/create/', ApplicationCreateView.as_view(), name='application-create'),
    path('applications/', ApplicationListView.as_view(), name='application-list'),
]
