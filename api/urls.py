from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from .views import PostView,RegisterView, LoginView, LikeView
urlpatterns = [
    path('post',PostView.as_view() ),
    path('register',RegisterView.as_view()),
    path('login',LoginView.as_view()),
    path('like',LikeView.as_view()),

]