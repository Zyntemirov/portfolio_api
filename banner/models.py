from django.db import models

# Create your models here.
class Banner(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d')

    def __str__(self):
        return self.title