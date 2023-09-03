from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllView, name='home'),
    path('<int:pk>/like/', views.LikeView, name='like_view'),
    path('<int:pk>/', views.AboutView, name='about'),
    path('<int:pk>/edit/', views.EditView, name='edit'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
]
