# Generated by Django 2.0 on 2019-05-18 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20190508_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='maxBedRooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='maxPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='minimumBedRooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='minLand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='minPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Seeker',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f0',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f1',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f10',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f11',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f12',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f13',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f14',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f15',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f16',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f17',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f18',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f19',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f2',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f20',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f21',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f22',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f23',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f24',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f25',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f26',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f27',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f29',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f3',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f30',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f4',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f5',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f6',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f7',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f8',
        ),
        migrations.RemoveField(
            model_name='poster',
            name='f9',
        ),
        migrations.AddField(
            model_name='poster',
            name='Air_conditioning',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poster',
            name='Alarm_system',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poster',
            name='Balcony',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poster',
            name='Bathrooms',
            field=models.CharField(choices=[('Any', 'Any'), ('1+', '1+'), ('2+', '2+'), ('3+', '3+'), ('4+', '4+'), ('5+', '5+')], default='', max_length=10),
        ),
        migrations.AddField(
            model_name='poster',
            name='Broadband',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poster',
            name='Built_in_robes',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poster',
            name='Car_spaces',
            field=models.CharField(choices=[('Any', 'Any'), ('1+', '1+'), ('2+', '2+'), ('3+', '3+'), ('4+', '4+'), ('5+', '5+')], default='', max_length=10),
        ),
        migrations.AddField(
            model_name='poster',
            name='DishWasher',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poster',
            name='Ensuite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poster',
            name='Floorboards',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poster',
            name='Fully_fenced',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poster',
            name='Garage',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poster',
            name='Gym',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poster',
            name='Heating',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poster',
            name='High_energy_efficiency',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poster',
            name='Outdoor_area',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poster',
            name='Outdoor_spa',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poster',
            name='Rumpus_room',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poster',
            name='Shed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poster',
            name='Solar_hot_water',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poster',
            name='Solar_panels',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poster',
            name='Study',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poster',
            name='Swimming_pool',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poster',
            name='Tennis_court',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poster',
            name='Undercover_parking',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poster',
            name='Water_tank',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poster',
            name='Workshop',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='poster',
            name='new_or_established',
            field=models.CharField(choices=[('Any', 'Any'), ('New', 'New'), ('Established', 'Established')], default='', max_length=20),
        ),
        migrations.AddField(
            model_name='poster',
            name='Max_bedrooms',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='index.maxBedRooms'),
        ),
        migrations.AddField(
            model_name='poster',
            name='Max_price',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='index.maxPrice'),
        ),
        migrations.AddField(
            model_name='poster',
            name='Min_bedrooms',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='index.minimumBedRooms'),
        ),
        migrations.AddField(
            model_name='poster',
            name='Min_price',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='index.minPrice'),
        ),
        migrations.AddField(
            model_name='poster',
            name='Property_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='index.PropertyType'),
        ),
        migrations.AddField(
            model_name='poster',
            name='min_land_size',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='index.minLand'),
        ),
    ]
