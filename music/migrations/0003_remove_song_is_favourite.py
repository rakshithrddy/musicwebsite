# Generated by Django 2.0.7 on 2018-07-24 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_is_favourite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='is_favourite',
        ),
    ]
