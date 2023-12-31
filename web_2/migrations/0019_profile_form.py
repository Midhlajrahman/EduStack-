# Generated by Django 4.2.5 on 2023-11-02 04:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web_2", "0018_rename_date_d_playlist_head_d_date_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="profile_form",
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
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("pic", models.FileField(upload_to="media")),
            ],
        ),
    ]
