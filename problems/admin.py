from django.contrib import admin

# Register your models here.

from.models import App, Cause, Location, ProblemType, Problem, Title
admin.site.register(Problem)
admin.site.register(ProblemType)
admin.site.register(Location)
admin.site.register(Cause)
admin.site.register(App)
admin.site.register(Title)