from django.urls import path
from . import views
from .views import CreateSkillView,UpdateSkillView,SkillDeleteView

urlpatterns = [

    path('login/', views.loginUser, name = "login"),
    path('logout/', views.logoutUser , name = "logout"),
    path('register/',views.registerUser, name = "register"),
    path('account/', views.userAccount, name = 'account'),
    path('edit-account/', views.editAccount, name = "edit-account"),
    path('create-skill/',CreateSkillView.as_view(), name = "create-skill"),
    path('update-skill/<str:pk>/' ,UpdateSkillView.as_view(), name = "update-skill"),
    path('delete-skill/<str:pk>/',SkillDeleteView.as_view(), name = "delete-skill"),

    path('',views.profiles , name = "profiles"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('inbox/', views.inbox, name = "inbox"),
    path('message/<str:pk>/', views.viewMessage, name = "message"),
    path('send-message/<str:pk>/',views.createMessage,name="create-message"),

   
] 