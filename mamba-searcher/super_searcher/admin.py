from django.contrib import admin
from .models import File, FilteredFiles

admin.site.register(File)
admin.site.register(FilteredFiles)
