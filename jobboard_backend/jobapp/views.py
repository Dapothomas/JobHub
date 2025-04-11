from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication, permissions
from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.db import connection

from .models import Job, Category
from .serializers import JobSerializer, JobDetailSerializer, CategorySerializer
from .forms import JobForm

def health_check(request):
    try:
        # Test database connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
        
        return JsonResponse({
            'status': 'healthy',
            'database': 'connected'
        }, status=200)
    except Exception as e:
        return JsonResponse({
            'status': 'unhealthy',
            'error': str(e)
        }, status=500)

class UserDetailView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        # Get the authenticated user
        user = request.user
        
        # Return user details including user_type
        return Response({
            'id': user.id,
            'email': user.email,
            'username': user.username,
            'user_type': user.user_type,  
            'company_name': user.company_name, 
            'profile_description': user.profile_description  
        })
    
class CategoriesView(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializers = CategorySerializer(categories, many=True)
        
        return Response(serializers.data)

class NewestJobsView(APIView):
    def get(self, request, format=None):
        jobs = Job.objects.all()[0:4]
        serializers = JobSerializer(jobs, many=True)
        
        return Response(serializers.data)

class MyJobsView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, format=None):
        jobs = Job.objects.filter(created_by=request.user)
        serializers = JobSerializer(jobs, many=True)
        return Response(serializers.data)
    
    
class CreateJobView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        form = JobForm(request.data)
         
        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()
            
            return Response({'status': 'Job created successfully'})
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        # try:
            job = Job.objects.get(pk=pk, created_by=request.user)
            job.delete()
            return Response({'status': 'Job deleted successfully'})
        # except Job.DoesNotExist:
        #     return Response({'error': 'Job not found'}, status=404)
        
    def put(self, request, pk):
        job = Job.objects.get(pk=pk, created_by=request.user)
        form = JobForm(request.data, instance=job)
        if form.is_valid():
            form.save()
            return Response({'status': 'Job updated successfully'})
        return Response(form.errors, status=400)

class BrowseJobsView(APIView):
    def get(self, request, format=None):
        jobs = Job.objects.all()
        categories = request.GET.get('categories', '')
        query = request.GET.get('query', '')
        
        print("Received categories:", categories)
        print("Type of categories:", type(categories))
        
        if query:
            jobs = jobs.filter(title__icontains=query) 
            
        if categories:
            category_ids = categories.split(',')
            print("Split category IDs:", category_ids)
            jobs = jobs.filter(category__id__in=category_ids)
            print("SQL Query:", jobs.query)
            print("Filtered jobs count:", jobs.count())
        
        serializers = JobSerializer(jobs, many=True)
        return Response(serializers.data)
    
class JobDetailView(APIView):
    def get(self, request, pk, format=None):
        job = Job.objects.get(pk=pk)
        serializers = JobDetailSerializer(job)
        
        return Response(serializers.data)
