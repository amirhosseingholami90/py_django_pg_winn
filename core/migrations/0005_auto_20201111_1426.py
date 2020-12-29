# Generated by Django 3.0.8 on 2020-11-11 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200702_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeValue',
            fields=[
                ('code_value', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('definition', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('display', models.CharField(max_length=100)),
                ('active_ind', models.BooleanField(default=True, verbose_name='Active')),
                ('active_dt_tm', models.DateTimeField(blank=True, null=True)),
                ('begin_effective_dt_tm', models.DateTimeField(blank=True, null=True, verbose_name='Begin Effective Date/Time')),
                ('end_effective_dt_tm', models.DateTimeField(blank=True, null=True, verbose_name='End Effective Date/Time')),
                ('inactivate_dt_tm', models.DateTimeField(blank=True, null=True)),
                ('display_sequence', models.IntegerField(default=0)),
                ('wki', models.CharField(blank=True, max_length=255, null=True, verbose_name='WKI')),
                ('concept_wki', models.CharField(blank=True, max_length=255, null=True, verbose_name='Concept WKI')),
                ('wdf_meaning', models.CharField(blank=True, max_length=16, null=True, verbose_name='Meaning')),
                ('create_dt_tm', models.DateTimeField(auto_now_add=True)),
                ('create_id', models.BigIntegerField(default=0)),
                ('updt_cnt', models.IntegerField(default=0)),
                ('updt_dt_tm', models.DateTimeField(auto_now=True)),
                ('updt_id', models.BigIntegerField(default=0)),
            ],
            options={
                'db_table': 'core_code_value',
            },
        ),
        migrations.CreateModel(
            name='CodeValueSet',
            fields=[
                ('code_set', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('display', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('definition', models.CharField(max_length=100)),
                ('active_ind', models.BooleanField(default=True, verbose_name='Active')),
                ('cache_ind', models.BooleanField(default=False, verbose_name='Cached')),
                ('change_access_ind', models.BooleanField(default=True, verbose_name='Change Allowed ')),
                ('create_dt_tm', models.DateTimeField(auto_now_add=True)),
                ('create_id', models.BigIntegerField(default=0)),
                ('updt_cnt', models.IntegerField(default=0)),
                ('updt_dt_tm', models.DateTimeField(auto_now=True)),
                ('updt_id', models.BigIntegerField(default=0)),
            ],
            options={
                'db_table': 'core_code_value_set',
            },
        ),
        migrations.AlterField(
            model_name='item',
            name='active_status_cd',
            field=models.CharField(choices=[('01', 'Active'), ('02', 'Combined'), ('03', 'Historical value - combined'), ('04', 'Deleted'), ('05', 'Draft'), ('06', 'Inactive'), ('07', 'Recall'), ('08', 'Review'), ('09', 'Suspended'), ('10', 'Unknown')], default='01', max_length=2, verbose_name='Active Status'),
        ),
        migrations.AddIndex(
            model_name='codevalueset',
            index=models.Index(fields=['code_set'], name='cvs_code_set_idx'),
        ),
        migrations.AddIndex(
            model_name='codevalueset',
            index=models.Index(fields=['display'], name='cvs_display_idx'),
        ),
        migrations.AddField(
            model_name='codevalue',
            name='code_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cv_code_values', to='core.CodeValueSet'),
        ),
        migrations.AddIndex(
            model_name='codevalue',
            index=models.Index(fields=['code_set'], name='cv_code_set_idx'),
        ),
        migrations.AddIndex(
            model_name='codevalue',
            index=models.Index(fields=['display'], name='cv_display_idx'),
        ),
    ]