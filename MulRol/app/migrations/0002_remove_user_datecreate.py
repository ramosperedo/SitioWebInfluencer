# Generated by Django 3.0.7 on 2020-07-20 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='dateCreate',
        ),
    ]
