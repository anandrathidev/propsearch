# Generated by Django 2.0 on 2019-05-19 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20190515_0546'),
    ]

    operations = [
        migrations.AddField(
            model_name='createprofile',
            name='select_category',
            field=models.CharField(choices=[('Individual', 'Individual'), ('Agency', 'Agency')], default='Individual', max_length=30),
            preserve_default=False,
        ),
    ]