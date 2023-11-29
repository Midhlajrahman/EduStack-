# Generated by Django 4.2.7 on 2023-11-28 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0065_rename_course_playlisthead_course_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="video",
            name="Course",
        ),
        migrations.AddField(
            model_name="video",
            name="Playlist",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="web.playlist",
            ),
            preserve_default=False,
        ),
    ]