# Generated by Django 4.2.3 on 2023-08-02 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0004_alter_course_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='meta',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='seo',
            field=models.TextField(null=True),
        ),
    ]
