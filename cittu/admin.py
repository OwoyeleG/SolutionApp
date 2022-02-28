from django.contrib import admin
from.models import *

# Register your models here.
from.models import SubUnitReport, ReportType
admin.site.register(SubUnitReport)
admin.site.register(ReportType)