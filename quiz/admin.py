from django.contrib import admin
from .models import Quiz, QuizCategories, QuizQuestion, QuizAnswer, QuizAttempt, QuizScore

# Register your models here.


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_by', 'category', 'max_questions']
    list_display_links = ['id', 'title',
                          'created_by', 'category', 'max_questions']


@admin.register(QuizCategories)
class QuizCategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']


@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'quiz']
    list_display_links = ['id', 'question']
    list_filter = ['quiz']


@admin.register(QuizAnswer)
class QuizAnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'answer', 'quiz', 'question', 'is_correct']
    list_display_links = ['id', 'answer']
    list_filter = ['quiz', 'question']


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ['id', 'marks', 'quiz',
                    'user', 'question', 'selected_answer']
    list_display_links = ['id', 'quiz']
    list_filter = ['quiz', 'user']


@admin.register(QuizScore)
class QuizScoreAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'quiz',
                    'obtained_marks', 'has_passed']
    list_display_links = ['id', 'quiz', 'user']
    list_filter = ['quiz', 'user']
