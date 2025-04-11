from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import health_check


from . import views


urlpatterns = [
    path('categories/', views.CategoriesView.as_view()),
    path('health/', health_check),
    path('newest/', views.NewestJobsView.as_view()),
    path('myjobs/', views.MyJobsView.as_view()),
    path('<int:pk>/delete/', views.CreateJobView.as_view()),
    path('create/', views.CreateJobView.as_view()),
    path('<int:pk>/edit/', views.CreateJobView.as_view()),
    path('browsejobs/', views.BrowseJobsView.as_view()),
    path('users/me/', views.UserDetailView.as_view(), name='user-detail'),
    path('<int:pk>/', views.JobDetailView.as_view()),
]