# Generated by Django 4.0.3 on 2024-08-15 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0003_answer_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='author',
        ),
    ]
