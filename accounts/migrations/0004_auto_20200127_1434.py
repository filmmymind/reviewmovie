# Generated by Django 3.0 on 2020-01-27 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200127_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_image',
            field=models.ImageField(default="{%static 'image/userprofile.png' %}", upload_to=''),
        ),
    ]
