# Generated by Django 3.0 on 2020-01-13 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0005_auto_20200113_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewmovie',
            name='score',
            field=models.FloatField(blank=True, default='', null=True),
        ),
    ]