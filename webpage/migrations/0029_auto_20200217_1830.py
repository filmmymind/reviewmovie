# Generated by Django 3.0 on 2020-02-17 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0028_ratingmovie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingmovie',
            name='score',
            field=models.FloatField(blank=True, null=True),
        ),
    ]