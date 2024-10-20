from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import User
from .serializers import UserSerializer, UserLoginSerializer, UserViewSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

class UserRegisterView(generics.CreateAPIView):
    """This handles a user signing up"""
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = serializer.instance
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        }, status=status.HTTP_201_CREATED)

class UserLoginView(APIView):
    """
    Handles user login and returns a token if authentication is successful.
    """
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data, context={'request': request})
        
        # Validate the serializer
        if serializer.is_valid():
            user = serializer.validated_data['user']
            
            # Generate or retrieve a token for the user
            token, created = Token.objects.get_or_create(user=user)
            
            # Return the token and user details as a response
            return Response({
                'token': token.key,
                'username': user.username,
                'email': user.email
            }, status=status.HTTP_200_OK)
        
        # If validation fails, return the error messages
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(APIView):
    """
    This retrieves user information using the token sent with the request
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self, request):
            user = request.user
            serializer = UserViewSerializer(user)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
