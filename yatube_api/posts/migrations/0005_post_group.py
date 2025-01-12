# Generated by Django 3.2.16 on 2025-01-12 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_follow_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='posts.group'),
        ),
    ]
