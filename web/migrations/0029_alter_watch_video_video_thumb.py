# Generated by Django 4.2.5 on 2023-10-19 07:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0028_alter_bootstrap_playlist_video_thumbnail"),
    ]

    operations = [
        migrations.AlterField(
            model_name="watch_video",
            name="video_thumb",
            field=models.FileField(upload_to="media"),
        ),
    ]
