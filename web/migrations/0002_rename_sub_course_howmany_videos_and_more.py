# Generated by Django 4.2.5 on 2023-09-10 12:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="course",
            old_name="sub",
            new_name="howmany_videos",
        ),
        migrations.RenameField(
            model_name="course",
            old_name="videosnum",
            new_name="video_title",
        ),
    ]
