from django.urls import path
from . import views
from .views import CreateSkillView,UpdateSkillView,SkillDeleteView,MessageDetailView,CreateMessageView,EditAccountView
urlpatterns = [

    path('login/', views.loginUser, name = "login"),
    path('logout/', views.logoutUser , name = "logout"),
    path('register/',views.registerUser, name = "register"),
    path('account/', views.userAccount, name = 'account'),
    path('edit-account/', EditAccountView.as_view(), name = "edit-account"),
    path('create-skill/',CreateSkillView.as_view(), name = "create-skill"),
    path('update-skill/<str:pk>/' ,UpdateSkillView.as_view(), name = "update-skill"),
    path('delete-skill/<str:pk>/',SkillDeleteView.as_view(), name = "delete-skill"),

    path('',views.profiles , name = "profiles"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('inbox/', views.inbox, name = "inbox"),
    path('message/<str:pk>/', MessageDetailView.as_view(), name = "message"),
    path('send-message/<str:pk>/',CreateMessageView.as_view(),name="create-message"),

   
] 