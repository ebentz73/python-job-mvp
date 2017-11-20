# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-11-20 04:46
from __future__ import unicode_literals

from django.db import migrations, models
from django.db.models import F
import django.utils.timezone


def forwards_func(apps, schema_editor):
    job = apps.get_model("website", "Job")
    db_alias = schema_editor.connection.alias
    job.objects.using(db_alias).all().update(created_at=F('created_date'))


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_connection_feedback'),
    ]

    operations = [
        migrations.RunSQL('SET CONSTRAINTS ALL IMMEDIATE',
                          reverse_sql=migrations.RunSQL.noop),
        migrations.AddField(
            model_name='job',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.RunPython(forwards_func, atomic=True),
        migrations.RunSQL(migrations.RunSQL.noop,
                          reverse_sql='SET CONSTRAINTS ALL IMMEDIATE'),
    ]
