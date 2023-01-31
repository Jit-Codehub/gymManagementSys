from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField()
