from django.db import models


class File(models.Model):
    file = models.FileField(upload_to='files/', null=True)

    def __str__(self):
        return self.file


class FilteredFiles(models.Model):
    filtered_files = models.FileField(upload_to='filtered_files/', null=True)

    def __str__(self):
        return self.filtered_files

