from django.db import models
# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    icon = models.CharField(max_length=40)

    def __str__(self):
        return self.title


class Success(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    icon = models.CharField(max_length=40)

    def __str__(self):
        return self.title
