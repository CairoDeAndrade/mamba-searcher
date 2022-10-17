from django.contrib import admin
from .models import File, FilteredFiles, Images

admin.site.register(File)
admin.site.register(FilteredFiles)
admin.site.register(Images)
