# Generated by Django 3.0.7 on 2020-07-29 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itrac', '0007_auto_20200727_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='resolved_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
