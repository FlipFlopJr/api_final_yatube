# Generated by Django 3.2.16 on 2025-01-12 20:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_follow_group'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('user', 'following')},
        ),
    ]