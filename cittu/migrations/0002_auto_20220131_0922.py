# Generated by Django 3.2.7 on 2022-01-31 08:22

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cittu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subunitreport',
            name='achievement',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='subunitreport',
            name='challenge',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='subunitreport',
            name='conclusion',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='subunitreport',
            name='introduction',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='subunitreport',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
