# Generated by Django 4.0.3 on 2022-07-24 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_user_userdb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdb',
            name='private_key',
        ),
    ]
