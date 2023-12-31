# Generated by Django 4.2.5 on 2023-10-04 15:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0013_playlist"),
    ]

    operations = [
        migrations.CreateModel(
            name="watch_video",
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
                ("video", models.ImageField(upload_to="media")),
                ("video_thumb", models.ImageField(upload_to="media")),
                ("title", models.CharField(max_length=50)),
                ("date", models.CharField(max_length=50)),
                ("tutor_image", models.ImageField(upload_to="media")),
                ("tutor_name", models.CharField(max_length=50)),
                ("tutor_position", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=100)),
            ],
        ),
    ]
