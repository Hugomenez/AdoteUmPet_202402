# Generated by Django 5.0.3 on 2024-05-06 17:04

import utils.idrandom
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userprofile", "0004_alter_profile_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="id",
            field=models.UUIDField(
                default=utils.idrandom.random_id,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]