# Generated by Django 5.1 on 2024-09-03 15:15

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Answer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", ckeditor.fields.RichTextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("deleted_at", models.DateTimeField(default=None, null=True)),
                ("votes_count", models.IntegerField(default=0)),
                (
                    "downvote",
                    models.ManyToManyField(
                        related_name="downupvote_answer", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]
