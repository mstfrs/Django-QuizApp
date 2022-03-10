from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from .models import Answer, Category, Question, Quiz
from .serializers import CategorySerializer, QuestionSerializer, QuizSerializer
from rest_framework import viewsets, status


class Categories(APIView):
    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        quiz = Category.objects.get(pk=pk)
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        quiz = Category.objects.get(pk=pk)
        quiz.delete()
        data = {
            "message": "Succesfully deleted"
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


class QuizView(APIView):

    def get(self, request, category, *args, **kwargs):
        queryset = Quiz.objects.filter(category=category)
        serializer = QuizSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        quiz = Quiz.objects.get(pk=pk)
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        quiz = Quiz.objects.get(pk=pk)
        quiz.delete()
        data = {
            "message": "Succesfully deleted"
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


class QuestionView(APIView):

    def get(self, request, title, *args, **kwargs):
        queryset = Question.objects.filter(quiz=title)
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        quiz = Question.objects.get(pk=pk)
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        quiz = Question.objects.get(pk=pk)
        quiz.delete()
        data = {
            "message": "Succesfully deleted"
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
