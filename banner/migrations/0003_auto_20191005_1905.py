# Generated by Django 2.2.6 on 2019-10-05 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0002_auto_20191005_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(max_length=1000, upload_to=''),
        ),
    ]
