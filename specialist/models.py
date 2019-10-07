import PIL
from PIL import Image
from django.db import models

# for creating
from for_image import give_name, resize_image
# for deleting
from django.db.models.signals import *
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Specialist(models.Model):
    name = models.CharField(max_length=50)
    profile = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=15)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(max_length=1000)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.image.name = give_name(self.image.name, 'specialist/150')
        super(Specialist, self).save(*args, **kwargs)
        img1 = Image.open(self.image)

        img1 = img1.resize((150, 150), PIL.Image.ANTIALIAS)
        img1.save(self.image.path)

@receiver(post_delete, sender=Specialist)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

####################################################################################

class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField(default=50, validators=[MaxValueValidator(100), MinValueValidator(1)])
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE, related_name='skills')

    def __str__(self):
        return self.name
