# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-28 10:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dao', '0003_auto_20160922_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='p_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_comments', to='dao.Comment'),
        ),
    ]
