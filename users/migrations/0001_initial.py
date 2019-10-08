# Generated by Django 2.2.6 on 2019-10-08 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user_account', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('user_id', models.CharField(max_length=20)),
                ('user_sex', models.IntegerField(default=1)),
                ('user_password', models.CharField(max_length=20)),
                ('user_nickname', models.CharField(max_length=20)),
                ('user_img', models.ImageField(upload_to='upload/users/')),
                ('user_isdelete', models.BooleanField(default=False)),
                ('user_isactive', models.BooleanField(default=False)),
                ('token', models.CharField(max_length=50)),
                ('vcode', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
