from rest_framework import serializers
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.password_validation import validate_password
from .models import User
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
   
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username').strip()
        password = data.get('password').strip()

        if username and password:
            user = authenticate(request=self.context.get('request'), username=username, password=password)
            if not user:
                raise serializers.ValidationError('Invalid username or password.')
        else:
            raise serializers.ValidationError('Must include "username" and "password".')

        data['user'] = user
        return data
