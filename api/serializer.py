from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields=["user","slug","likes","title","description"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ["username", "password"]


