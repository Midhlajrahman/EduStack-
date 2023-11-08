# Generated by Django 4.2.5 on 2023-09-20 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_selectbox_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_image', models.ImageField(upload_to='media')),
                ('teacher_name', models.CharField(max_length=50)),
                ('teacher_position', models.CharField(max_length=50)),
                ('insta_url', models.CharField( max_length=50)),
                ('wp_url' ,models.CharField( max_length=50)),
                ( 'linkedin_url',models.CharField( max_length=50)),

            ],
        ),
        migrations.DeleteModel(
            name='web_course',
        ),
    ]
