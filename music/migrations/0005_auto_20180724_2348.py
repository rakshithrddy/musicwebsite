# Generated by Django 2.0.7 on 2018-07-24 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_song_is_favourite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='is_favourite',
            new_name='is_favorite',
        ),
    ]
