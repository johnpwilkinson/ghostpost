# Generated by Django 3.1 on 2020-08-21 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GhostPostApp', '0002_auto_20200821_0258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='post_or_roast',
            new_name='boast_or_roast',
        ),
    ]
