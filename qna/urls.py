from django.urls import path
from .views import index,signup,PostQuestion,QuestionDetail,add_answer_to_question,logout_view


urlpatterns = [
    path('',index,name = 'index'),
    path('signup/',signup,name = 'signup'),
    path('qpost/',PostQuestion.as_view(),name = 'post'),
    path('detail/<int:pk>/',QuestionDetail.as_view(), name = 'detail'),
    path('detail/<int:pk>/answer/',add_answer_to_question,name = 'answer'),
    path('logout/',logout_view,name = 'logout'),
    ]
