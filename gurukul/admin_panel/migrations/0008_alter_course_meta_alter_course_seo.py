# Generated by Django 4.2.3 on 2023-08-02 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0007_alter_course_meta_alter_course_seo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='meta',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='seo',
            field=models.TextField(default=None, null=True),
        ),
    ]
