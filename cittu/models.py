from django.db import models

from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class ReportType(models.Model):
    title = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = True, auto_now=False)

    def __str__(self):
        return str(self.title)

class SubUnitReport(models.Model):
    report_type =    models.ForeignKey('ReportType', on_delete=models.CASCADE)
    introduction =   models.TextField(blank=True)
    achievement =    models.TextField(blank=True)
    challenge =      models.TextField(blank=True)
    conclusion =     models.TextField(blank=True)
    date_from =      models.DateTimeField(auto_now_add = True, auto_now=False)
    date_to =        models.DateTimeField(auto_now_add = True, auto_now=False)
    created_by =     models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date_created =   models.DateTimeField(auto_now_add = True, auto_now=False)

    def __str__(self):
        return str(self.report_type)


