# Generated by Django 3.2 on 2021-05-01 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutpage',
            name='footer',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='subHeading',
        ),
    ]
