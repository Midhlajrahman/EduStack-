# Generated by Django 4.2.5 on 2023-11-02 23:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web_2", "0021_alter_profile_form_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile_form",
            name="image",
            field=models.FileField(blank=True, null=True, upload_to="images"),
        ),
    ]
