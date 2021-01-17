# Generated by Django 3.1.4 on 2021-01-17 03:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import itrac.models.issue_attachment


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itrac', '0028_auto_20210115_2221'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issueattachment',
            options={'ordering': ['-uploaded_at'], 'verbose_name': 'issue_attachment', 'verbose_name_plural': 'issue_attachments'},
        ),
        migrations.AlterField(
            model_name='issueattachment',
            name='attachment',
            field=models.FileField(upload_to=itrac.models.issue_attachment.get_directory_path, validators=[itrac.models.issue_attachment.validate_file_size], verbose_name='Choose a file to upload'),
        ),
        migrations.AlterField(
            model_name='issueattachment',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='issueattachment',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
