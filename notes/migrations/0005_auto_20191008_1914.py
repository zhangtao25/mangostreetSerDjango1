# Generated by Django 2.2.6 on 2019-10-08 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20191008_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='cover',
            field=models.ImageField(upload_to='avatars/'),
        ),
        migrations.AlterField(
            model_name='note',
            name='images',
            field=models.ImageField(upload_to='avatars/'),
        ),
    ]
