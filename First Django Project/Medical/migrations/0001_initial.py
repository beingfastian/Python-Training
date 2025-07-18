# Generated by Django 5.2.4 on 2025-07-16 20:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('facility_type', models.CharField(choices=[('hospital', 'Hospital'), ('clinic', 'Clinic'), ('pharmacy', 'Pharmacy')], max_length=20)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('stock_quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=20, unique=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='pending', max_length=20)),
                ('total_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Medical.facilities')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Medical.patient')),
            ],
        ),
        migrations.CreateModel(
            name='ShipmentItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Medical.prescription')),
                ('shipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Medical.shipment')),
            ],
        ),
        migrations.AddField(
            model_name='shipment',
            name='medicines',
            field=models.ManyToManyField(through='Medical.ShipmentItem', to='Medical.prescription'),
        ),
    ]
