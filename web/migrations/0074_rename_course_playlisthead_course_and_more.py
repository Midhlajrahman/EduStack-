# Generated by Django 4.2.7 on 2023-11-29 05:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0073_playlist_playlist_head_video_video_thumb"),
    ]

    operations = [
        migrations.RenameField(
            model_name="playlisthead",
            old_name="course",
            new_name="Course",
        ),
        migrations.AddField(
            model_name="course",
            name="prerequisites",
            field=models.ManyToManyField(blank=True, to="web.course"),
        ),
        migrations.AddField(
            model_name="course",
            name="topic",
            field=models.CharField(
                choices=[
                    ("html", "HTML"),
                    ("css", "CSS"),
                    ("js", "JavaScript"),
                    ("bootstrap", "Bootstrap"),
                    ("react", "React"),
                    ("python", "Python"),
                    ("psql", "PostgreSQL"),
                ],
                default=1,
                max_length=20,
            ),
            preserve_default=False,
        ),
    ]
