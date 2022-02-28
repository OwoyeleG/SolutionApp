from django.db import models

from django.contrib.auth.models import User


# Create your models here.


# problem types.
class ProblemType(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title


# location table.
class Location(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title


# app table.
class App(models.Model):
    app_name = models.TextField(max_length=50)

    def __str__(self) -> str:
        return self.app_name


# title table.
class Title(models.Model):
    title = models.TextField(max_length=50)
    app = models.ForeignKey(App, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


# problem table.
class Problem(models.Model):
    app                = models.ForeignKey(App, on_delete=models.CASCADE)
    problem_type = models.ForeignKey(ProblemType, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, default=1, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    answered    = models.BooleanField(default=False)
    attempted = models.BooleanField(default=False)
    adopted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# cause table.
class Cause(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    cause = models.TextField(max_length=150)

    def __str__(self) -> str:
        return self.cause

