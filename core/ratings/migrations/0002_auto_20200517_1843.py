# Generated by Django 3.0.5 on 2020-05-17 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='rating_name',
            new_name='rating_title',
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating_creation_date',
            field=models.DateTimeField(verbose_name='Rating creation date'),
        ),
    ]