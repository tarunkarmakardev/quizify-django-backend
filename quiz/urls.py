from django.urls import path, include
from .views import QuizAPIView, QuizQuestionAPIView, QuizAnswerAPIView, QuizAttemptStatusAPIView, QuizAttemptAPIView, QuizScoreSaveAPIView, QuizScoreAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('quiz', QuizAPIView, basename='quiz')


urlpatterns = [
    # Quiz List and Quiz Details
    path('', include(router.urls)),
    #     Quiz Questions List
    path('quiz/questions/<int:quiz_pk>/',
         QuizQuestionAPIView.as_view({'get': 'list'}), name='quiz_questions_list'),
    #     Quiz Question details
    path('quiz/questions/<int:quiz_pk>/<int:ques_pk>/',
         QuizQuestionAPIView.as_view({'get': 'retrieve'}), name='quiz_question_detail'),
    #     Quiz Answers List
    path('quiz/answers/<int:quiz_pk>/<int:ques_pk>/',
         QuizAnswerAPIView.as_view(), name='quiz_answers_list'),
    #     Quiz Attempt Status view
    path('quiz/attempt/status/<int:quiz_pk>/<int:ques_pk>/',
         QuizAttemptStatusAPIView.as_view(), name='quiz_attempt_status'),
    #     Quiz Attempt view
    path('quiz/attempt/<int:quiz_pk>/<int:ques_pk>/',
         QuizAttemptAPIView.as_view(), name='quiz_attempt'),
    path('quiz/save/<int:quiz_pk>/',
         QuizScoreSaveAPIView.as_view(), name='quiz_score_save'),
    path('quiz/show/scores/',
         QuizScoreAPIView.as_view(), name='quiz_score_scores')

]
