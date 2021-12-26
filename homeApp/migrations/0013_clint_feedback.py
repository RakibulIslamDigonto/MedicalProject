# Generated by Django 4.0 on 2021-12-26 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0012_alter_doctor_doc_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clint_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cli_name', models.CharField(max_length=50, verbose_name='Client Name')),
                ('cli_designation', models.CharField(max_length=50, verbose_name='Client Designation')),
                ('cli_feedback', models.TextField()),
                ('cli_image', models.ImageField(blank=True, upload_to='dep_images/')),
            ],
        ),
    ]
