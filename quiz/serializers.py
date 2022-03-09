from django.db.models import fields
from rest_framework import serializers, validators
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer

from quiz.models import Answer, Category, Question, Quiz


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class QuizSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Quiz
        fields = [
            "title",
            "category",

        ]


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = [
            "id",
            "answer_text",
            "is_right"
        ]


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    def get_answers(self, obj):
        serializer = AnswerSerializer(obj.question, many=True)
        return (serializer.data)

    class Meta:
        model = Question
        fields = ["id", "title", "difficulty", "answers"]
