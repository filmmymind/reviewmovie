# Generated by Django 3.0 on 2020-01-12 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webboard', '0002_auto_20200112_1023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boardpost',
            name='author',
        ),
    ]
