# Generated by Django 2.1.7 on 2019-03-07 13:30

from django.db import migrations

import core.managers.user


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', core.managers.user.UserManager()),
                ('objects_all', core.managers.user.UserManager(alive_only=False)),
            ],
        ),
    ]
