from django.db.models import fields
from rest_framework import serializers, validators
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer

from quiz.models import Answer, Category, Question, Quiz


class CategorySerializer(serializers.ModelSerializer):
    quiz_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ("name", "quiz_count")

    def get_quiz_count(self, obj):
        return obj.category.count()


class QuizSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    question_count = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = ("title", "category", "question_count")

    def get_question_count(self, obj):
        return obj.quiz.count()


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
