from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django_group_model.models import AbstractGroup


class Employee(AbstractUser):
    groups = models.ManyToManyField(
        'accounts.Group',
        verbose_name="groups",
        blank=True,
        help_text=(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name="user_set",
        related_query_name="user",

    )

class Group(AbstractGroup):
    # You can add custom fields here
    name = CharField(max_length=50, unique=False)
