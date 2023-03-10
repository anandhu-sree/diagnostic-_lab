# Generated by Django 4.1.4 on 2023-01-04 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labapp', '0002_userregmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='apoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('department', models.CharField(max_length=50)),
            ],
        ),
    ]
