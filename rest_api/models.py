from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    """
    The person creating tasks.
    """
    username = models.CharField(max_length=50, null=False, unique=True)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(null=False, max_length=50)

    class Meta:
        ordering = ['username']

    def __str__(self):
        return self.username


class Task(models.Model):
    """
    Just something a User wants to accomplish.
    """
    owner = models.ManyToManyField(User)
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500, blank=False)
    task_start_date = models.DateTimeField()
    task_end_date = models.DateTimeField()
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.description