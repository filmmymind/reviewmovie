# Generated by Django 3.0 on 2020-01-19 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0026_auto_20200119_1322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='replytext',
        ),
    ]
