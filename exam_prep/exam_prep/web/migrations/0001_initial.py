# Generated by Django 4.0.2 on 2022-02-21 19:43

import django.core.validators
from django.db import migrations, models

import exam_prep.web.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Expense",
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
            ],
        ),
        migrations.CreateModel(
            name="Profile",
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
                (
                    "first_name",
                    models.CharField(
                        max_length=15,
                        validators=[
                            django.core.validators.MinLengthValidator(2),
                            exam_prep.web.models.validate_only_letters,
                        ],
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        max_length=15,
                        validators=[
                            django.core.validators.MinLengthValidator(2),
                            exam_prep.web.models.validate_only_letters,
                        ],
                    ),
                ),
                (
                    "budget",
                    models.FloatField(
                        default=0,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="profiles/",
                        validators=[exam_prep.web.models.MaxFileSizeInMbValidator(5)],
                    ),
                ),
            ],
        ),
    ]
