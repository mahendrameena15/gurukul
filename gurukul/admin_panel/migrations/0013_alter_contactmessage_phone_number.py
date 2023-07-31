# Generated by Django 4.2.3 on 2023-07-31 09:08

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0012_alter_contactmessage_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
