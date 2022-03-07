from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from .models import Category, Quiz
from .serializers import CategorySerializer, QuizSerializer
from rest_framework import viewsets


class Categories(APIView):
    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class QuizView(APIView):
    def get_obj(self, category):
        return get_object_or_404(Quiz, category=category)

    def get(self, request, category):
        queryset = Category.objects.filter(category)
        serializer = QuizSerializer(queryset, many=True)
        return Response(serializer.data)


# class QuizView(viewsets.ModelViewSet):
#     queryset = Quiz.objects.all()
#     serializer_class = QuizSerializer
