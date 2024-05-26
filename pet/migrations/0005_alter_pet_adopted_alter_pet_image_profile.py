# Generated by Django 5.0.6 on 2024-05-26 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pet", "0004_alter_pet_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet",
            name="adopted",
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name="pet",
            name="image_profile",
            field=models.ImageField(upload_to="pets/profile/imagesPets/%Y/%m/"),
        ),
    ]
