from rest_framework import serializers
from accounts.models import Profile
from posts.models import Post as UserPost
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = UserPost


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, data):
        user = User.objects.create_user(username=data['username'], password=data['password'])
        user.save()
        profile = Profile.objects.create(user=user)
        profile.save()
        return user


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPost
        fields = ['image', 'description']

    def create_post(self, data):
        post = UserPost.objects.create(image=data['image'], description=data['description'])
        post.save()
        return post
