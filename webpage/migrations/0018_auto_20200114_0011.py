# Generated by Django 3.0 on 2020-01-13 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0017_auto_20200114_0008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewmovie',
            name='image_height',
        ),
        migrations.AlterField(
            model_name='reviewmovie',
            name='movie_image',
            field=models.ImageField(upload_to='image'),
        ),
    ]