# Generated by Django 4.0 on 2021-12-23 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0003_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='skill_Quantity',
            field=models.IntegerField(),
        ),
    ]
