# Generated by Django 5.1.1 on 2024-10-30 20:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_rename_place_name_rented_rental_rented_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defectivevehiclereport',
            name='vehicle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.vehicle'),
        ),
    ]
