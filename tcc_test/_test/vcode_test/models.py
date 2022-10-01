from django.db import models


class File(models.Model):
    filepath = models.FileField(upload_to='files/')

    def __str__(self):
        return self.filepath
