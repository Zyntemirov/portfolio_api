import PIL
from PIL import Image
from django.db import models

# for creating
from for_image import give_name, resize_image
# for deleting
from django.db.models.signals import *
from django.dispatch import receiver

# Create your models here.
class Feedback(models.Model):
    autor_name = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    autor_image = models.ImageField(max_length=1000)

    def __str__(self):
        return self.autor_name

    def save(self, *args, **kwargs):
        self.autor_image.name = give_name(self.autor_image.name, 'feedback/150')
        super(Feedback, self).save(*args, **kwargs)
        img1 = Image.open(self.autor_image)

        img1 = img1.resize((150, 150), PIL.Image.ANTIALIAS)
        img1.save(self.autor_image.path)

@receiver(post_delete, sender=Feedback)
def submission_delete(sender, instance, **kwargs):
    instance.autor_image.delete(False)
