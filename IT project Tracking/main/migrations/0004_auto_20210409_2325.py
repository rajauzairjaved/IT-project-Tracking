# Generated by Django 2.2.16 on 2021-04-09 18:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210409_2324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='tutorial_content',
            new_name='project_content',
        ),
        migrations.RemoveField(
            model_name='project',
            name='tutorial_published',
        ),
        migrations.AddField(
            model_name='project',
            name='project_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 9, 23, 25, 17, 109243), verbose_name='date published'),
        ),
    ]
