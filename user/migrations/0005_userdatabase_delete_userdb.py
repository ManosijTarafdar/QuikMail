# Generated by Django 4.1.7 on 2023-05-10 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_userdb_private_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='userDatabase',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('firstName', models.CharField(default='userFirstName', max_length=50)),
                ('lastName', models.CharField(default='userLastName', max_length=50)),
                ('dateOfBirth', models.DateField()),
                ('phoneNumber', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='userDB',
        ),
    ]