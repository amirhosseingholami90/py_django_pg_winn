# Generated by Django 3.0.7 on 2020-08-22 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itrac', '0019_auto_20200821_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='slug',
        ),
        migrations.AddField(
            model_name='project',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
