from rest_framework import generics
from .serializers import PostSerializer, UserCreateSerializer, UsersSerializer, PostCreateSerializer
from accounts.models import Profile
from rest_framework import status
from rest_framework.response import Response
from posts.models import Post as UserPost


# Create your views here.
class AllPostView(generics.ListCreateAPIView):
    queryset = UserPost.objects.all()
    serializer_class = PostSerializer


class AboutPostView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserPost.objects.all()
    serializer_class = PostSerializer


class AllUserView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = UsersSerializer


class AboutUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UsersSerializer

    def get_queryset(self):
        user = self.request.user
        return Profile.objects.filter(user=user)


class register_user(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

    def register_user(self):
        if self.request.method == 'POST':
            serializer = UserCreateSerializer(data=self.request.data)
            if serializer.is_valid():
                serializer.save()
                profile = Profile.objects.create_user(user=self.request.user)
                profile.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostView(generics.CreateAPIView):
    serializer_class = PostCreateSerializer

    def create_post(self):
        if self.request.method == "POST":
            serializer = PostCreateSerializer(data=self.request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
