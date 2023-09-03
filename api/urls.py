from django.urls import path
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('', views.AllPostView.as_view()),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path("schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("schema/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path('create/', views.PostView.as_view()),
    path('<int:pk>/', views.AboutPostView.as_view()),
    path('users/', views.AllUserView.as_view()),
    path('users/<int:pk>/', views.AboutUserView.as_view()),
    path('users/create/', views.register_user.as_view())
]
