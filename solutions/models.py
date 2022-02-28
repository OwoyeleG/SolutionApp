from django.db import models
from problems.models import Problem
from django.contrib.auth.models import User
# Create your models here.

class Solution(models.Model):
    #test_solution         = models.TextField(max_length=50)
    solution              = models.TextField(max_length=250)
    problem               = models.ForeignKey(Problem, on_delete=models.CASCADE)
    date_created          = models.DateTimeField(auto_now_add=True, auto_now=False)
    created_by            = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)



    def __str__(self) -> str:
        return self.solution
