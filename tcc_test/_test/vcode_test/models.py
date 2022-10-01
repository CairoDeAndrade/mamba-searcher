from django.db import models


class File(models.Model):
    filepath = models.FileField(upload_to='files/', null=True, verbose_name="")

    def __str__(self):
        return self.filepath
