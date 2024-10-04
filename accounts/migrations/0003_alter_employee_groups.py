# Generated by Django 4.2.1 on 2024-06-24 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_employee"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="user_set",
                related_query_name="user",
                to="accounts.group",
                verbose_name="groups",
            ),
        ),
    ]