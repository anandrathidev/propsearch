# Generated by Django 2.0 on 2019-05-20 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20190520_0530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='category',
            field=models.CharField(choices=[('Buyer', 'Buyer'), ('Seller', 'Seller')], default='', max_length=30),
        ),
    ]