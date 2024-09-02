# Generated by Django 5.1 on 2024-08-31 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "questions",
            "0007_rename_tags_question_labels_question_follows_count_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="question",
            name="modified_at",
        ),
        migrations.AddField(
            model_name="question",
            name="deleted_at",
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="question",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
