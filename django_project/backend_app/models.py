from django.db import models
from django.contrib.auth.models import User
from app.models import Colleges


class Employee(User):
    college = models.OneToOneField(to=Colleges, on_delete=models.SET_NULL, null=True)
