# Generated by Django 4.0 on 2021-12-23 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0008_alter_department_galary_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='dep_image',
            field=models.ImageField(blank=True, upload_to='dep_images/'),
        ),
        migrations.AddField(
            model_name='department',
            name='dep_short_des',
            field=models.TextField(blank=True),
        ),
    ]
