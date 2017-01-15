# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-15 11:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170115_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='BucketListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=155)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('done', models.BooleanField(default=False)),
                ('date_modified', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='bucketlist',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='bucketlistitem',
            name='bucketlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.BucketList'),
        ),
    ]
