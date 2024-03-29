# Generated by Django 3.2 on 2021-05-06 11:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0003_quizanswer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name_plural': 'Quizzes'},
        ),
        migrations.AlterModelOptions(
            name='quizcategories',
            options={'verbose_name_plural': 'QuizCategories'},
        ),
        migrations.CreateModel(
            name='QuizAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField(verbose_name='Marks')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quizquestion')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz')),
                ('selected_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quizanswer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
