# Generated by Django 3.1 on 2020-08-21 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GhostPostApp', '0003_auto_20200821_0318'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='secret',
            field=models.CharField(default='JpYPVj', max_length=6),
        ),
    ]
