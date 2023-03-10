# Generated by Django 4.1.4 on 2023-01-04 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userregmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
