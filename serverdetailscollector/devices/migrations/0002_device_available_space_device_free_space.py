# Generated by Django 4.2.5 on 2023-09-23 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='available_space',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='device',
            name='free_space',
            field=models.IntegerField(default=-1),
        ),
    ]