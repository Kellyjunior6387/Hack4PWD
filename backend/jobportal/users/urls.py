from django.urls import path
from .views import UserRegisterView, UserLoginView, UserViewSet
urlpatterns = [
    path('signup' , UserRegisterView.as_view(), name='signup'),
    path('login', UserLoginView.as_view(), name='login' ),
    path('profile', UserViewSet.as_view(), name='profile')
]
