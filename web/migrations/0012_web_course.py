# Generated by Django 4.2.5 on 2023-10-02 11:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0011_teacher_profile_delete_web_course"),
    ]

    operations = [
        migrations.CreateModel(
            name="web_course",
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
                ("howmany_video", models.CharField(max_length=50)),
                ("video_title", models.CharField(max_length=50)),
                ("thumbnail", models.ImageField(upload_to="media")),
            ],
        ),
    ]
