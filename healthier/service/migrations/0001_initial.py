# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-27 08:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_prices.models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('providers', '0001_initial'),
        ('consumers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseHealthierService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=200)),
                ('details', models.CharField(default='', max_length=1000)),
                ('service_id', models.CharField(default='service_nxi4mr4cd3q9wsmhok45', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MeasuredTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lower_range', models.CharField(max_length=200)),
                ('upper_range', models.CharField(max_length=200)),
                ('measure_value', models.CharField(max_length=200)),
                ('measured_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.Provider')),
                ('measured_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consumers.Consumer')),
                ('service_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.BaseHealthierService')),
            ],
        ),
        migrations.CreateModel(
            name='OrderedService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(blank=True, choices=[('', 'Payment Status'), ('Paid', 'P'), ('Not Paid', 'NP')], max_length=200)),
                ('order_id', models.CharField(default='order_cait781w3la2ycwehbwr', max_length=200)),
                ('preferred_date', models.DateField(default=(('EVR', 'EVERYDAY'), ('MON', 'MONDAYS'), ('TUE', 'TUESDAYS'), ('WED', 'WEDNESDAYS'), ('THU', 'THURSDAYS'), ('FRI', 'FRIDAYS'), ('SAT', 'SATURDAYS'), ('SUN', 'SUNDAYS')))),
                ('preferred_time', models.CharField(max_length=200)),
                ('promo_code', models.CharField(max_length=200)),
                ('order_date', models.DateTimeField()),
                ('ordered_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consumers.Consumer')),
                ('provided_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='providers.Provider')),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.BaseHealthierService')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=200)),
                ('group_description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceGroupCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('category_description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_fields', jsonfield.fields.JSONField()),
                ('generated_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_sent', models.BooleanField(default=False)),
                ('file_upload', models.FileField(null=True, upload_to='uploads/%Y/%m/%d/')),
                ('generated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.Provider')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.ServiceGroup')),
                ('service_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.BaseHealthierService')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceReportGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('group_description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceRequests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateTimeField()),
                ('duration', models.CharField(max_length=200)),
                ('rate', models.CharField(max_length=200)),
                ('price', django_prices.models.PriceField(currency='NGN', decimal_places=2, default=0.0, max_digits=12)),
                ('is_ordered', models.BooleanField(default=False)),
                ('days_available', models.CharField(choices=[('EVR', 'EVERYDAY'), ('MON', 'MONDAYS'), ('TUE', 'TUESDAYS'), ('WED', 'WEDNESDAYS'), ('THU', 'THURSDAYS'), ('FRI', 'FRIDAYS'), ('SAT', 'SATURDAYS'), ('SUN', 'SUNDAYS')], default='EVR', max_length=200)),
                ('time_available', models.TimeField(default=datetime.time(16, 0), max_length=200)),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.Provider')),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.BaseHealthierService')),
            ],
        ),
        migrations.AddField(
            model_name='servicegroup',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.ServiceGroupCategory'),
        ),
        migrations.AddField(
            model_name='basehealthierservice',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.ServiceGroup'),
        ),
        migrations.AddField(
            model_name='basehealthierservice',
            name='provider_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='providers.Provider'),
        ),
    ]
