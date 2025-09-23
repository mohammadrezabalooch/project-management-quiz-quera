from django.db import models
from django.conf import settings


class RoleType(models.IntegerChoices):
    MEMBER = 0, "member"
    OWNER = 1, "owner"


class Category(models.Model):
    name = models.CharField(max_length=25)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through="Membership")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Membership(models.Model):
    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.IntegerField(choices=RoleType.choices)
