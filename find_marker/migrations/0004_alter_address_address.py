# Generated by Django 3.2.4 on 2021-06-29 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find_marker', '0003_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.TextField(null=True),
        ),
    ]