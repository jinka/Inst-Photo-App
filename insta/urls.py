from django.urls import path
from .views import ImageListView, ImageDetailView, ImageCreateView
from . import views

urlpatterns = [
    path('', ImageListView.as_view(), name='insta-home'),
    path('post/<int:pk>/', ImageDetailView.as_view(), name='insta-detail'),
    path('post/new/', ImageCreateView.as_view(), name='insta-create'),
    path('about/', views.about, name='insta-about'),
]
