# Generated by Django 4.2.5 on 2023-10-23 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_2', '0010_d_playlist_head'),
    ]

    operations = [
        migrations.CreateModel(
            name='d_watch_video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='media')),
                ('title', models.CharField(max_length=100)),
                ('tutor_name', models.CharField(max_length=50)),
                ('tutor_image', models.FileField(upload_to='media')),
                ('tutor_position', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
            ],
        ),
    ]