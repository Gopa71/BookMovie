# Generated by Django 5.0 on 2023-12-10 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('rate', models.CharField(max_length=250)),
                ('photo', models.ImageField(upload_to='mvpic')),
                ('bgphoto', models.ImageField(upload_to='bgppic')),
                ('screen', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('date_dur', models.CharField(max_length=100)),
                ('desc', models.TextField()),
            ],
        ),
    ]
