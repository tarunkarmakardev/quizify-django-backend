# Generated by Django 3.2 on 2021-05-06 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_quizquestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(verbose_name='Answer')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Is Correct Answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quizquestion')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz')),
            ],
        ),
    ]
