# Generated by Django 4.2.7 on 2023-11-28 11:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0066_remove_video_course_video_playlist"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="video",
            name="video_thumb",
        ),
    ]
