# Generated by Django 3.2 on 2021-05-03 08:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_useraccount_user_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserAccount',
            new_name='UserProfile',
        ),
    ]