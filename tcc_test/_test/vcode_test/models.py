from django.db import models


class Files(models.Model):
    file = models.FileField()