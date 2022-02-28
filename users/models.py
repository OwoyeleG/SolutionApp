from django.db import models
#from django.db.models.fields import BooleanField
from django.contrib.auth.models import User

# Create your models here.


class Unit(models.Model):
    units             = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.units



class UnitHead(models.Model):
    user               = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    unit               = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=True, null=True)
    active             = models.BooleanField(default=False)
    #date_created       = models.DateTimeField(auto_now_add=True, auto_now=False)
    #created_by         = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.user)
