# Generated by Django 4.2.1 on 2024-06-24 10:42

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Group",
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
                ("name", models.CharField(max_length=50)),
                (
                    "permissions",
                    models.ManyToManyField(
                        blank=True,
                        related_name="custom_group_set",
                        to="auth.permission",
                        verbose_name="permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "group",
                "verbose_name_plural": "groups",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.GroupManager()),
            ],
        ),
    ]