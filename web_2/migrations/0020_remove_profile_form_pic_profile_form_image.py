# Generated by Django 4.2.5 on 2023-11-02 04:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web_2", "0019_profile_form"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile_form",
            name="pic",
        ),
        migrations.AddField(
            model_name="profile_form",
            name="image",
            field=models.ImageField(default=1, upload_to="media"),
            preserve_default=False,
        ),
    ]
