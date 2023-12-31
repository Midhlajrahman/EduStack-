# Generated by Django 4.2.5 on 2023-10-23 04:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web_2", "0012_d_watch_video_video_thumb"),
    ]

    operations = [
        migrations.CreateModel(
            name="course_2",
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
                ("authername", models.CharField(max_length=50)),
                ("auther_image", models.ImageField(upload_to="media")),
                ("date", models.CharField(max_length=50)),
                ("howmany_videos", models.CharField(max_length=50)),
                ("video_title", models.CharField(max_length=50)),
                ("thumbnail", models.ImageField(upload_to="media")),
            ],
        ),
    ]
