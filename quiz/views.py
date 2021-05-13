from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from .serializers import QuizSerializer, QuizQuestionSerializer, QuizAnswerSerializer, QuizAttemptSerializer, QuizScoreSerializer, QuizCreateSerializer
from .models import Quiz, QuizAttempt, QuizQuestion, QuizAnswer, QuizScore, QuizCategories


# Create your views here.


class QuizAPIView(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated, DjangoModelPermissions)

    def list(self, request):

        query = Quiz.objects.all()
        if(bool(request.query_params.get('own'))):
            query = Quiz.objects.filter(created_by=request.user)

        serializer = QuizSerializer(query, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = QuizCreateSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response({'message': 'your quiz was created', 'quiz': serializer.data.get('quiz')}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuizQuestionAPIView(ModelViewSet):
    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionSerializer
    lookup_field = 'ques_pk'

    def list(self, request, quiz_pk):
        query = QuizQuestion.objects.filter(quiz__pk=quiz_pk).order_by('pk')
        question_ids = [item.id for item in query]

        return Response({"question_ids": question_ids}, status=status.HTTP_200_OK)

    def retrieve(self, request, quiz_pk, ques_pk):
        query = QuizQuestion.objects.get(pk=ques_pk, quiz__pk=quiz_pk)
        serializer = QuizQuestionSerializer(query)

        return Response(serializer.data, status=status.HTTP_200_OK)


class QuizAnswerAPIView(ListCreateAPIView):
    queryset = QuizAnswer.objects.all()
    serializer_class = QuizAnswerSerializer

    def get(self, request, quiz_pk, ques_pk):
        query = QuizAnswer.objects.filter(
            quiz__pk=quiz_pk, question__pk=ques_pk)
        answers = [{'id': item.id, 'answer': item.answer} for item in query]

        return Response({"answers": answers}, status=status.HTTP_200_OK)


class QuizAttemptAPIView(CreateAPIView):
    queryset = QuizAttempt.objects.all()
    serializer_class = QuizAttemptSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, quiz_pk, ques_pk):
        serializer = QuizAttemptSerializer(data=request.data, context={
                                           'quiz_pk': quiz_pk, 'ques_pk': ques_pk})
        if serializer.is_valid():
            serializer.save(user=request.user)
            serializer.data['attempted'] = True
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuizAttemptStatusAPIView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, quiz_pk, ques_pk, ):
        quiz = Quiz.objects.get(pk=int(quiz_pk))
        ques = QuizQuestion.objects.get(pk=int(ques_pk))
        user = request.user
        attempted_question = QuizAttempt.objects.filter(
            question=ques, quiz=quiz, user=user)
        attempted = attempted_question.exists()

        if attempted:
            selected_answer_id = attempted_question[0].selected_answer.pk
            correct_answer_id = QuizAnswer.objects.filter(
                question=ques, quiz=quiz, is_correct=True)[0].pk
            return Response({'attempted': attempted, 'selected_answer_id': selected_answer_id, 'correct_answer_id': correct_answer_id}, status=status.HTTP_302_FOUND)
        return Response({'attempted': attempted}, status=status.HTTP_304_NOT_MODIFIED)


class QuizScoreSaveAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, quiz_pk):
        quiz = Quiz.objects.get(pk=int(quiz_pk))
        user = request.user
        # Each question has 1 mark, hence total marks = total questions
        total_marks = quiz.max_questions
        obtained_marks = sum(
            [item.marks for item in QuizAttempt.objects.filter(quiz=quiz, user=user)])
        has_passed = (obtained_marks/total_marks > 0.6)
        response_data = {'quiz_id': quiz.pk, 'quiz_title': quiz.title,
                         'obtained_marks': obtained_marks, 'has_passed': has_passed}
        already_saved = QuizScore.objects.filter(quiz=quiz, user=user).exists()
        if already_saved:
            return Response(response_data, status=status.HTTP_200_OK)
        QuizScore.objects.create(
            quiz=quiz, user=user, obtained_marks=obtained_marks, has_passed=has_passed)
        return Response(response_data, status=status.HTTP_200_OK)


class QuizScoreAPIView(ListAPIView):
    serializer_class = QuizScoreSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return QuizScore.objects.filter(user=self.request.user)
