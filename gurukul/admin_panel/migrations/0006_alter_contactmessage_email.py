# Generated by Django 4.2.3 on 2023-07-31 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0005_contactmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
