# Generated by Django 3.0.8 on 2020-09-12 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_delete_personimport'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonImport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('number', models.IntegerField(null=True)),
                ('date', models.DateField(null=True)),
            ],
        ),
    ]
