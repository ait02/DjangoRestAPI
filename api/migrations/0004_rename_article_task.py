# Generated by Django 3.2 on 2021-05-20 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210520_1733'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Article',
            new_name='Task',
        ),
    ]
