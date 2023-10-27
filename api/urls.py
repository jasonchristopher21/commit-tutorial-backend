from django.urls import path
from . import views

urlpatterns = [
    path('post', views.PostList.as_view()),
    path('catfact', views.RandomCatFactView.as_view()),
]