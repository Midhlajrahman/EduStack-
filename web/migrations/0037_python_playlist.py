# Generated by Django 4.2.5 on 2023-10-20 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0036_python_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='python_playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_thumbnail', models.FileField(upload_to='media')),
                ('video_title', models.CharField(max_length=50)),
            ],
        ),
    ]