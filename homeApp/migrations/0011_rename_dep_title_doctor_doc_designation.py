# Generated by Django 4.0 on 2021-12-26 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0010_schedule_doctor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='dep_title',
            new_name='doc_designation',
        ),
    ]
