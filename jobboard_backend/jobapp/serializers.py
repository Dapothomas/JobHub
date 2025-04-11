from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth import get_user_model


from .models import Job, Category

User = get_user_model()

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password', 'user_type', 'company_name', 'profile_description')
        
class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'user_type', 'company_name', 'profile_description')

class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
        )

class JobSerializer (serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            'id',
            'title',
            'position_salary',
            'company_location',
            'company_name',
            'created_at_formatted',
        )
        
class JobDetailSerializer (serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            'id',
            'title',
            'category',
            'company_email',
            'description',
            'company_location',
            'position_salary',
            'position_location',
            'company_name',
            'created_at_formatted',
        )