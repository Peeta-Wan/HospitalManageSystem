# Generated by Django 3.0.5 on 2020-04-21 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_user_avator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='avator',
            new_name='avatar',
        ),
    ]
