from django.urls import path
from . import views
from .views import ProjectView,CreateProjectView,ProjectUpdateView

urlpatterns = [
    
    path('',views.projects, name = "projects"),
    path('project/<str:pk>/',  ProjectView.as_view(), name = "project"),
    path('create-project/', CreateProjectView.as_view(), name = "create-project"),
    path('update-project/<str:pk>/',ProjectUpdateView.as_view() , name = "update-project"),
    path('delete-project/<str:pk>/', views.deleteProject , name = "delete-project"),

]
