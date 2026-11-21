from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('movie/<int:pk>/', views.movie_detail_view, name='movie_detail'),
]