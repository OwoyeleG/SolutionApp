from solutions.models import Solution
from django.contrib import admin

# Register your models here.
from.models import Solution
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'solution')
admin.site.register(Solution, SolutionAdmin)