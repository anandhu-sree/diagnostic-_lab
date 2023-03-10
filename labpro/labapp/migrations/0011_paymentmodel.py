# Generated by Django 4.1.4 on 2023-01-17 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labapp', '0010_delete_paymentmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='paymentmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardnumber', models.IntegerField()),
                ('cvv', models.IntegerField()),
                ('email_id', models.CharField(max_length=30)),
                ('exp_date', models.DateField()),
                ('card_holder_name', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
