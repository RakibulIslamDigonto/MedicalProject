# Generated by Django 4.0 on 2021-12-23 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0007_department_department_galary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department_galary',
            name='department',
            field=models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, related_name='dep_gal', to='homeApp.department'),
        ),
    ]
