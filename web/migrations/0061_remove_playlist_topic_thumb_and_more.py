# Generated by Django 4.2.7 on 2023-11-28 09:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0060_alter_video_video"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="playlist",
            name="topic_thumb",
        ),
        migrations.RemoveField(
            model_name="playlist",
            name="topic_title",
        ),
    ]