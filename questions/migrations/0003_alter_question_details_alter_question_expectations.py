# Generated by Django 5.1 on 2024-08-28 08:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_delete_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='details',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(20, 'the field must contain at least 20 characters')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='expectations',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(20, 'the field must contain at least 20 characters')]),
        ),
    ]
