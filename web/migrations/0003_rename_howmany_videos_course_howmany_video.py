# Generated by Django 4.2.5 on 2023-09-10 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_rename_sub_course_howmany_videos_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='howmany_videos',
            new_name='howmany_video',
        ),
    ]
