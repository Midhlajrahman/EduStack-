# Generated by Django 4.2.7 on 2023-11-28 09:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0063_remove_playlisthead_playlist_playlisthead_course"),
    ]

    operations = [
        migrations.RenameField(
            model_name="playlist",
            old_name="Course",
            new_name="course",
        ),
        migrations.AddField(
            model_name="playlist",
            name="topic_thumb",
            field=models.ImageField(default=1, upload_to="media"),
            preserve_default=False,
        ),
    ]
