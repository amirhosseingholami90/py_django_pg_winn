# Generated by Django 3.0.4 on 2020-06-20 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200619_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdefinition',
            name='updt_appctx',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='itemdefinition',
            name='updt_cnt',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='itemdefinition',
            name='updt_id',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='itemdefinition',
            name='updt_task',
            field=models.BigIntegerField(default=0),
        ),
    ]
