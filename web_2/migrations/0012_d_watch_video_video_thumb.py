# Generated by Django 4.2.5 on 2023-10-23 03:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web_2", "0011_d_watch_video"),
    ]

    operations = [
        migrations.AddField(
            model_name="d_watch_video",
            name="video_thumb",
            field=models.FileField(default=1, upload_to="media"),
            preserve_default=False,
        ),
    ]
