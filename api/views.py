from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
from .serializer import PostSerializer, UserSerializer
from rest_framework import authentication, permissions
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .slug import generate_slug
from .models import Post
# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        if User.objects.filter(username=request.data["username"]).exists():
            return Response("user already exists")
        else:
            user= User.objects.create(username=request.data["username"], password=request.data["password"])
            user.set_password(request.data["password"])
            user.save()
            serializer = UserSerializer(user)
            return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data["username"], password=request.data["password"])
        if user:
            currentUser = User.objects.get(username=request.data["username"])
            token, created = Token.objects.get_or_create(user=currentUser)
            return Response({
                'token': token.key,
                'user_id': user.pk,

            })
        return Response("invalid credentials")



class PostView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    #create post
    def post(self, request):
        request.data['slug']= generate_slug(request.data['title'])
        request.data['user']=request.user.pk
        print(request.data)
        ser = PostSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    # get posts made by the user
    def get(self, request):
        post_made_by_user = Post.objects.filter(user=request.user.pk)
        print(post_made_by_user.values()[:])
        return Response(post_made_by_user.values()[:])



    #edit post made by the user
    def put(self, request):
        post =  Post.objects.get(id=request.query_params['id'])
        if post.user == request.user:
            if "title" in request.data:
                request.data['slug'] = generate_slug(request.data['title'])

            post.__dict__.update(request.data)
            post.save()
            serializer = PostSerializer(post)
            return Response(serializer.data)
        else:
            return Response("you're not allowed to edit this post")


    #delete post made by the user
    def delete(self,request):
        try:
            post = Post.objects.get(id=request.query_params['id'])
            if post.user == request.user:
                post.delete()
                return Response("post deleted")
            else:
                return Response("you're not allowed to delete this post")


        except:
            return Response("post not found")



#like another user's post


class LikeView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        currentUser = str(request.user)
        post = Post.objects.get(id=request.query_params['id'])
        if currentUser in post.likes:
            return Response("You already liked this post")
        else:
            post.likes.append(currentUser)
            post.save()
            serializer = PostSerializer(post)
            return Response(serializer.data)





