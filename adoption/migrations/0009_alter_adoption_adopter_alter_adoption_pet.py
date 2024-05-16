# Generated by Django 5.0.3 on 2024-05-06 19:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adoption", "0008_alter_adoption_id"),
        ("pet", "0010_alter_pet_owner"),
        ("userprofile", "0006_alter_profile_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="adoption",
            name="adopter",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="adopted_pets",
                to="userprofile.profile",
            ),
        ),
        migrations.AlterField(
            model_name="adoption",
            name="pet",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="pet.pet"
            ),
        ),
    ]