# Generated by Django 4.2.7 on 2023-11-29 05:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0074_rename_course_playlisthead_course_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="playlisthead",
            old_name="Course",
            new_name="course",
        ),
        migrations.RemoveField(
            model_name="course",
            name="prerequisites",
        ),
        migrations.RemoveField(
            model_name="course",
            name="topic",
        ),
    ]
