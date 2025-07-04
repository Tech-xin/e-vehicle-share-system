# Generated by Django 5.1.1 on 2024-10-30 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_defectivevehiclereport'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rental',
            old_name='place_name',
            new_name='place_name_rented',
        ),
        migrations.AddField(
            model_name='rental',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rental',
            name='place_name_returned',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
