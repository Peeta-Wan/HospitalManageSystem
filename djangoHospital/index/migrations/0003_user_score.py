# Generated by Django 3.0.5 on 2020-04-20 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='score',
            field=models.FloatField(default=0.0),
        ),
    ]