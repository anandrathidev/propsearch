# Generated by Django 2.0 on 2019-05-21 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_auto_20190521_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='select',
            field=models.CharField(blank=True, choices=[('Individual', 'Individual'), ('Agency', 'Agency')], max_length=30),
        ),
    ]
