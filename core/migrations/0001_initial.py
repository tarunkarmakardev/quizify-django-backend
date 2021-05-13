# Generated by Django 3.2 on 2021-05-01 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100, verbose_name='About page Heading')),
                ('subHeading', models.CharField(blank=True, max_length=100, null=True, verbose_name='About page Sub Heading')),
                ('body', models.TextField(blank=True, null=True)),
                ('footer', models.CharField(max_length=200, verbose_name='About page footer text')),
            ],
        ),
    ]
