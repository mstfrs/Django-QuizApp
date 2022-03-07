
from django.urls import path, include
from rest_framework import routers
from quiz.views import Categories, QuizView


# router = routers.DefaultRouter()
# router.register('', QuizView)

urlpatterns = [

    #    path('register/',RegisterAPI.as_view() ),
    path('', Categories.as_view()),
    path('<category>/', QuizView.as_view()),

]
