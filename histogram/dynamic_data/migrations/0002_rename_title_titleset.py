# Generated by Django 4.1.5 on 2023-01-09 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_data', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Title',
            new_name='TitleSet',
        ),
    ]
