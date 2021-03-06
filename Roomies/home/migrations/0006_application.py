# Generated by Django 2.0.4 on 2018-05-26 23:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0005_friend_current_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='-', max_length=50)),
                ('last_name', models.CharField(default='-', max_length=50)),
                ('email', models.EmailField(default='-', max_length=50)),
                ('bedtime', models.CharField(default='-', max_length=50)),
                ('graduating_class', models.CharField(default='NA', max_length=50)),
                ('major', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
