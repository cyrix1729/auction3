from django.urls import path
from . import views
from .views import user_api, listings_api

urlpatterns = [
    path('', views.index, name='index'),
    path('api/listings/<str:searchData>', listings_api, name="listings api"),
    path('api/user', user_api),
    path('getUsersQuestions/<int:user_id>/', views.getUserQuestions, name='questions'),
    path('getQuestion/<int:itemId>', views.getQuestion, name='view question'),
    path('postAnswer/<int:question_id>', views.postAnswer, name='submit answer'),
    path('postQuestion/<int:item_id>', views.postQuestion, name='submit question'),
    path('postItem', views.postItem, name='make listing'),
    path('getItem/<int:item_id>', views.getItem, name='view listing'),
    path('getQuestionsAskedToUser/<int:user_id>', views.getQuestionsAskedToUser, name='get questions on your items'),
    path('placeBid/<int:item_id>', views.placeBid, name='Place Bid')
]