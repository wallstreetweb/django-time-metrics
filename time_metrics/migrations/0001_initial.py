# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 16:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayMetric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('date_up', models.DateField(default=datetime.date.today)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'day metric',
                'verbose_name_plural': 'day metrics',
            },
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=90)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'metric',
                'verbose_name_plural': 'metrics',
            },
        ),
        migrations.CreateModel(
            name='MetricItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('date_up', models.DateField(default=datetime.date.today)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('metric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='time_metrics.Metric')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            options={
                'verbose_name': 'metric item',
                'verbose_name_plural': 'metric items',
            },
        ),
        migrations.CreateModel(
            name='MonthMetric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('date_up', models.DateField(default=datetime.date.today)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('metric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='time_metrics.Metric')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            options={
                'verbose_name': 'month metric',
                'verbose_name_plural': 'month metrics',
            },
        ),
        migrations.CreateModel(
            name='QuarterMetric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('date_up', models.DateField(default=datetime.date.today)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('metric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='time_metrics.Metric')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            options={
                'verbose_name': 'querter metric',
                'verbose_name_plural': 'quarter metrics',
            },
        ),
        migrations.CreateModel(
            name='WeekMetric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('date_up', models.DateField(default=datetime.date.today)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('metric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='time_metrics.Metric')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            options={
                'verbose_name': 'week metric',
                'verbose_name_plural': 'week metrics',
            },
        ),
        migrations.CreateModel(
            name='YearMetric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('date_up', models.DateField(default=datetime.date.today)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('metric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='time_metrics.Metric')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            options={
                'verbose_name': 'year metric',
                'verbose_name_plural': 'year metrics',
            },
        ),
        migrations.AddField(
            model_name='daymetric',
            name='metric',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='time_metrics.Metric'),
        ),
        migrations.AddField(
            model_name='daymetric',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
        ),
    ]
