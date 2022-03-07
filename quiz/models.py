from turtle import title
from django.db import models

# Create your models here.

class Category(models.Model):

    
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Quiz(models.Model):
    title=models.CharField(max_length=100)
    date_created=models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
class Question(models.Model):
    DIFFICULTY_CHOICES=[
        ( 'Easy','Easy'),
        ('Normal','Normal' ),
        ('Hard','Hard' ),
    ]
    title=models.CharField(max_length=300)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    difficulty=models.CharField(max_length=30, choices=DIFFICULTY_CHOICES)
    quiz = models.ForeignKey(Quiz, related_name='quiz', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Answer(models.Model):
    answer_text=models.CharField(max_length=100)
    is_right=models.BooleanField()
    date_updated=models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question, related_name='question', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.answer_text
    

    
