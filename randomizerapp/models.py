from django.db import models


class Result(models.Model):
    text = models.CharField(max_length=200)
