# Generated by Django 2.0.4 on 2018-05-29 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20180529_2316'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_pic',
        ),
    ]
