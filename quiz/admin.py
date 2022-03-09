from dataclasses import fields
from django.contrib import admin
from .models import Category, Quiz, Question, Answer
import nested_admin


class InLineAnswer(nested_admin.NestedTabularInline):
    model = Answer
    extra = 4
    max_num = 4


class InLineQuestion(nested_admin.NestedTabularInline):
    model = Question
    inlines = [InLineAnswer]
    extra = 1
    max_num = 1


class QuizAdmin(nested_admin.NestedModelAdmin):
    inlines = [InLineQuestion]
    list_display = ["title", "category", "date_created"]
    list_filter = ("title", "category")


admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Answer)
