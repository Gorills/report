from pyexpat import model
from django.contrib import admin

from .models import Project, Report, Dates, Group, Word, Position, Works, SearchEngine, Files
 
# Register your models here.


admin.site.register(Project)
admin.site.register(Report)
admin.site.register(Dates)
admin.site.register(Group)
admin.site.register(Word)
admin.site.register(Position)
admin.site.register(Works)
admin.site.register(SearchEngine)
admin.site.register(Files)
 