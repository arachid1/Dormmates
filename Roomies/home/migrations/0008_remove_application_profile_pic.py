# Generated by Django 2.0.4 on 2018-05-30 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_application_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='profile_pic',
        ),
    ]
