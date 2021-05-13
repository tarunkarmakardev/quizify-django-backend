from django.db.models import fields
from rest_framework import serializers
from .models import Quiz, QuizCategories, QuizQuestion, QuizAnswer, QuizAttempt, QuizScore


class QuizSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField()
    created_by = serializers.CharField(
        read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Quiz
        fields = "__all__"


class QuizCreateSerializer(serializers.Serializer):
    quiz = serializers.DictField()
    data = serializers.ListField(
        child=serializers.DictField()
    )

    def create(self, validated_data):
        # print('\033[93m' + str(validated_data) + '\033[0m')
        quiz_data = validated_data.get('quiz')
        category_data = quiz_data.get('category')
        questions_data = validated_data.get('data')
        category, created = QuizCategories.objects.get_or_create(
            name=category_data)
        quiz = Quiz.objects.create(title=quiz_data['quiz_name'], created_by=validated_data['created_by'],
                                   category=category, max_questions=quiz_data['max_questions'])
        for data in questions_data:
            question = QuizQuestion.objects.create(
                question=data['question'], quiz=quiz)
            answers_data = data.get('answers')
            for data in answers_data:
                QuizAnswer.objects.create(
                    quiz=quiz, question=question, answer=data['answer'], is_correct=data['is_correct'])
        return validated_data


class QuizQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuizQuestion
        fields = "__all__"


class QuizAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuizAnswer
        fields = '__all__'


class QuizAttemptSerializer(serializers.Serializer):
    selected_answer_id = serializers.IntegerField()

    def create(self, validated_data):
        quiz = Quiz.objects.get(pk=int(self.context['quiz_pk']))
        ques = QuizQuestion.objects.get(pk=int(self.context['ques_pk']))
        selected_answer = QuizAnswer.objects.get(
            pk=validated_data['selected_answer_id'])
        marks = 0
        if QuizAnswer.objects.get(pk=selected_answer.pk).is_correct:
            marks = 1
        user = validated_data.pop('user')
        try:
            attempt = QuizAttempt.objects.create(
                user=user, quiz=quiz, question=ques, selected_answer=selected_answer, marks=marks)
        except:
            raise serializers.ValidationError(
                {'selected_answer_id': f'Already answered by {user.username}!', 'attempted': True})
        return attempt


class QuizScoreSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer()

    class Meta:
        model = QuizScore
        fields = ['quiz', 'obtained_marks', 'has_passed']
