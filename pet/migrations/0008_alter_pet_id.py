# Generated by Django 5.0.3 on 2024-05-06 17:06

import utils.idrandom
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pet", "0007_alter_pet_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet",
            name="id",
            field=models.IntegerField(
                default=utils.idrandom.random_id,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]