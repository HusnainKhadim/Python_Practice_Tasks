from django.db import models


class Files(models.Model):
    filterd_file = models.FileField(null=True, blank=True, upload_to='files/')
