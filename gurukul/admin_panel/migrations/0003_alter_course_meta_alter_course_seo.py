# Generated by Django 4.2.3 on 2023-08-02 09:10

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0002_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='meta',
            field=jsonfield.fields.JSONField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='seo',
            field=jsonfield.fields.JSONField(max_length=200, null=True),
        ),
    ]
