from django.db.models import fields
from rest_framework import serializers, validators
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer

from quiz.models import Category, Question, Quiz


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class QuizSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Quiz
        fields = "__all__"
        
        
class QuestionSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Question
        fields = "__all__"
