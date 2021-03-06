# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-16 01:35
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import portal.fields.percentage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=50)),
                ('building', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('county', models.CharField(blank=True, max_length=50)),
                ('zip_code', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('office_phone', models.CharField(blank=True, max_length=25)),
                ('mobile_phone', models.CharField(blank=True, max_length=25)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('dob', models.DateField(blank=True, null=True)),
                ('note', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Deductible',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(unique=True)),
            ],
            options={
                'ordering': ('value',),
            },
        ),
        migrations.CreateModel(
            name='Insured',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('office_phone', models.CharField(blank=True, max_length=25)),
                ('mobile_phone', models.CharField(blank=True, max_length=25)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('dob', models.DateField(blank=True, null=True)),
                ('note', models.TextField(blank=True)),
                ('title_other', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Limit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min', models.PositiveIntegerField()),
                ('max', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ('min', 'max'),
            },
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('performs', models.BooleanField(default=False)),
                ('work_percentage', portal.fields.percentage.PercentageField(default=0, validators=django.core.validators.MaxValueValidator(100))),
                ('note', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
                ('practice_percentage', portal.fields.percentage.PercentageField(default=0, validators=django.core.validators.MaxValueValidator(100))),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('abbr', models.CharField(max_length=2, unique=True)),
                ('counties', models.ManyToManyField(to='portal.County')),
                ('limits', models.ManyToManyField(to='portal.Limit')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('address_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portal.Address')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('office_phone', models.CharField(blank=True, max_length=25)),
                ('note', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=('portal.address',),
        ),
        migrations.AddField(
            model_name='insured',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Title'),
        ),
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.State'),
        ),
        migrations.AddField(
            model_name='agent',
            name='agency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Agency'),
        ),
    ]
