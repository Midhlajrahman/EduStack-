# Generated by Django 4.2.5 on 2023-10-12 09:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0019_alter_playlist_topic_title"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="playlist",
            name="topic_description",
        ),
        migrations.RemoveField(
            model_name="playlist",
            name="topic_title",
        ),
        migrations.AddField(
            model_name="playlist_head",
            name="topic_description",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="playlist_head",
            name="topic_title",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
