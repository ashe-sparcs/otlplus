# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-27 07:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subject', '0001_initial'),
        ('session', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(null=True)),
                ('semester', models.SmallIntegerField(null=True)),
                ('table_id', models.SmallIntegerField(null=True)),
                ('lecture', models.ManyToManyField(to='subject.Lecture')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timetable_set', to='session.UserProfile')),
            ],
        ),
    ]