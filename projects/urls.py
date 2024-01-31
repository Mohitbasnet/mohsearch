from django.urls import path
from . import views
from .views import ProjectView

urlpatterns = [
    
    path('',views.projects, name = "projects"),
    path('project/<str:pk>/',  ProjectView.as_view(), name = "project"),
    path('create-project/', views.createProject, name = "create-project"),
    path('update-project/<str:pk>/', views.updateProject , name = "update-project"),
    path('delete-project/<str:pk>/', views.deleteProject , name = "delete-project"),

]
