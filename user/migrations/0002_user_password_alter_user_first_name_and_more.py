# Generated by Django 4.0.3 on 2022-07-23 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='userPassword', max_length=1024),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='userFirstName', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='userLastName', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='private_key',
            field=models.CharField(default='userPrivateKey', max_length=1024),
        ),
    ]
