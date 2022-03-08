from django.urls import path
from quiz.views import Categories
from .views import QuizView



urlpatterns = [   
    path('', Categories.as_view()),
    path('<category>/', QuizView.as_view()),

]