# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-04 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dev_model', '0003_auto_20160904_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='devmodel',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feature',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
