# Generated by Django 2.0.5 on 2020-04-16 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('s_admin', '0003_restauranttypemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantModel',
            fields=[
                ('restro_id', models.AutoField(primary_key=True, serialize=False)),
                ('restro_name', models.CharField(max_length=30, unique=True)),
                ('restro_contact', models.IntegerField(unique=True)),
                ('restro_email', models.EmailField(max_length=100, unique=True)),
                ('restro_password', models.CharField(max_length=30)),
                ('restro_otp', models.IntegerField()),
                ('restro_status', models.CharField(default=False, max_length=30)),
                ('restro_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s_admin.AreaModel')),
                ('restro_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s_admin.RestaurantTypeModel')),
            ],
        ),
    ]
