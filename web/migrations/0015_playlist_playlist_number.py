# Generated by Django 4.2.5 on 2023-10-05 03:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0014_watch_video"),
    ]

    operations = [
        migrations.AddField(
            model_name="playlist",
            name="playlist_number",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
