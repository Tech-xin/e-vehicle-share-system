# Generated by Django 5.1.1 on 2024-10-30 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_rename_place_name_rental_place_name_rented_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rental',
            old_name='place_name_rented',
            new_name='rented_at',
        ),
        migrations.RenameField(
            model_name='rental',
            old_name='place_name_returned',
            new_name='returned_at',
        ),
    ]
