# Generated by Django 4.2.5 on 2023-09-14 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_contact_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='selectbox_course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
            ],
        ),
    ]