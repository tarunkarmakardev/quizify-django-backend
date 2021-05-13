from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class QuizCategories(models.Model):
    name = models.CharField('Name', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'QuizCategories'


class Quiz(models.Model):
    title = models.CharField('Title', max_length=100)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Created By')
    category = models.ForeignKey(
        QuizCategories, on_delete=models.CASCADE, verbose_name='Category')
    max_questions = models.IntegerField('Maximum number of questions')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Quizzes'


class QuizQuestion(models.Model):
    question = models.TextField('Question')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class QuizAnswer(models.Model):
    answer = models.TextField('Answer')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    is_correct = models.BooleanField('Is Correct Answer', default=False)

    def __str__(self):
        return self.answer


class QuizAttempt(models.Model):
    marks = models.IntegerField('Marks')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    selected_answer = models.ForeignKey(QuizAnswer, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['quiz', 'question']

    def __str__(self):
        return str(self.user)


class QuizScore(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    obtained_marks = models.IntegerField(
        'Obtained Marks', blank=True, null=True)
    has_passed = models.BooleanField('Passed')

    def __str__(self):
        return str(self.user)
