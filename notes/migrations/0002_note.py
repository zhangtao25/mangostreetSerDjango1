# Generated by Django 2.2.6 on 2019-10-08 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('normal', 'normal'), ('video', 'video')], default='normal', max_length=10)),
                ('desc', models.CharField(max_length=255)),
                ('likes', models.BooleanField(default=False)),
                ('cover', models.CharField(max_length=255)),
                ('user_id', models.CharField(max_length=50)),
                ('collects', models.IntegerField(default=0)),
                ('images', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]