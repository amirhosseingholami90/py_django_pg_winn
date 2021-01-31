# Generated by Django 3.1.4 on 2021-01-31 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itrac', '0031_auto_20210130_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('01', 'Open'), ('02', 'Investigate'), ('03', 'Await Approval'), ('10', 'Build in DEV'), ('11', 'Validating in DEV'), ('19', 'Ready for STAGING'), ('20', 'Build in STAGING'), ('21', 'Validating in STAGING'), ('29', 'Ready for PROD'), ('30', 'Build in PROD'), ('31', 'Validating in PROD'), ('32', 'Validated in PROD'), ('80', 'Complete'), ('90', 'Closed')], default='01', max_length=2),
        ),
    ]
