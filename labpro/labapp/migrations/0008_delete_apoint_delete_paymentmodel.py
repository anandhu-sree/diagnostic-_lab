# Generated by Django 4.1.4 on 2023-01-17 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labapp', '0007_alter_services_model_test_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='apoint',
        ),
        migrations.DeleteModel(
            name='paymentmodel',
        ),
    ]
