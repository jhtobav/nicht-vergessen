# Generated by Django 3.0.5 on 2020-05-10 00:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20200509_1930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='note_text',
            new_name='note_content',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='note_name',
            new_name='note_title',
        ),
        migrations.RemoveField(
            model_name='note',
            name='note_created_date',
        ),
        migrations.AddField(
            model_name='note',
            name='note_last_updated_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last time updated'),
            preserve_default=False,
        ),
    ]
