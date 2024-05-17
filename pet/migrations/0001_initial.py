# Generated by Django 5.0.3 on 2024-05-16 17:47

import django.db.models.deletion
import utils.idrandom
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("userprofile", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pet",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        default=utils.idrandom.random_id,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "species",
                    models.CharField(
                        choices=[("DOG", "Dog"), ("CAT", "Cat")], max_length=20
                    ),
                ),
                ("breed", models.CharField(max_length=255)),
                ("age", models.IntegerField()),
                ("color", models.CharField(max_length=255)),
                ("sex", models.CharField(max_length=255)),
                ("size", models.IntegerField()),
                ("weight", models.IntegerField()),
                ("history", models.TextField()),
                ("observations", models.TextField()),
                (
                    "image_profile",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="pets/profile/imagesPets/%Y/%m/",
                    ),
                ),
                ("adopted", models.BooleanField()),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pets",
                        to="userprofile.profile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MedicalRecord",
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
                ("castreated", models.BooleanField()),
                ("vaccines", models.BooleanField()),
                ("vaccine_description", models.TextField()),
                ("dewormed", models.BooleanField()),
                ("dewormer_description", models.TextField()),
                ("medical_history", models.TextField()),
                (
                    "id_pet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="medical_records",
                        to="pet.pet",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ImagesPets",
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
                    "image_pets",
                    models.ImageField(
                        blank=True, null=True, upload_to="pets/photos/imagesPets/%Y/%m/"
                    ),
                ),
                (
                    "id_pet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ImagesPets",
                        to="pet.pet",
                    ),
                ),
            ],
        ),
    ]
