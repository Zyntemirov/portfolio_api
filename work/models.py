import PIL
from PIL import Image
from django.db import models
from django.utils import timezone

# for creating
from for_image import give_name, resize_image
# for deleting
from django.db.models.signals import *
from django.dispatch import receiver

# Create your models here.
class Work(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    image = models.ImageField(max_length=1000)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.image.name = give_name(self.image.name, 'work/854')
        super(Work, self).save(*args, **kwargs)
        img1 = Image.open(self.image)

        img1 = img1.resize((854, 537), PIL.Image.ANTIALIAS)
        img1.save(self.image.path)

@receiver(post_delete, sender=Work)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)
