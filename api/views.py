from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

from api.models import Post
from api.serializers import PostSerializer

from api.logic.generate_fact import get_random_cat_fact

class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class RandomCatFactView(APIView):
    def get(self, request):
        random_fact = get_random_cat_fact()
        return Response({'fact': random_fact})