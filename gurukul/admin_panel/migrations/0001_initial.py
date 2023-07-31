# Generated by Django 4.2.3 on 2023-07-31 13:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=10)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student_Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(default='', max_length=100)),
                ('parent_name', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('state', models.CharField(default='', max_length=100)),
                ('district', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=200)),
                ('phone_number', models.CharField(default='', max_length=10)),
                ('date_of_birth', models.DateField(null=True)),
                ('class_passed_in_2023', models.CharField(choices=[('5th', '5th'), ('6th', '6th'), ('7th', '7th'), ('8th', '8th'), ('9th', '9th'), ('10th', '10th')], max_length=10, null=True)),
                ('percentage_scored', models.DecimalField(decimal_places=2, default=0, max_digits=5, validators=[django.core.validators.MinValueValidator(0)])),
                ('language_medium', models.CharField(choices=[('English', 'English'), ('Hindi', 'Hindi'), ('Marathi', 'Marathi'), ('Bengali', 'Bengali'), ('Odia', 'Odia'), ('Other', 'Other')], max_length=20, null=True)),
                ('reason_for_choice', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
