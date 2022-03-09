from xml.etree.ElementInclude import include
from django.urls import path
from quiz.views import Categories
from .views import QuizView,QuestionView



urlpatterns = [   
    path('', Categories.as_view()),
    path('<category>/',QuizView.as_view()),
    path('<category>/<title>/',QuestionView.as_view()),
        
        

]

