# Generated by Django 5.0.7 on 2024-08-11 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('python_tutorial', '0003_pythontutorial_content_with_uploads_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pythontutorial',
            name='content_with_uploads',
        ),
    ]
