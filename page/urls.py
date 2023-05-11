from django.urls import path
from .views import HomePageView, AboutPageView, DetailPostPage

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('detail/<int:pk>/', DetailPostPage.as_view(), name='detail'),
]