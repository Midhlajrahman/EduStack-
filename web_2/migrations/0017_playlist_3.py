# Generated by Django 4.2.5 on 2023-10-24 04:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web_2", "0016_course_3"),
    ]

    operations = [
        migrations.CreateModel(
            name="playlist_3",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("video_thumbnail", models.FileField(upload_to="media")),
                ("video_title", models.CharField(max_length=50)),
            ],
        ),
    ]
