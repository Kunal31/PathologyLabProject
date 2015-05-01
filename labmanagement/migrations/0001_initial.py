# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('test_type', models.CharField(max_length=20)),
                ('quantity', models.FloatField(max_length=10)),
                ('color', models.CharField(max_length=20)),
                ('appearance', models.CharField(max_length=20)),
                ('Reaction', models.CharField(max_length=25)),
                ('cholestrol', models.FloatField(null=True, blank=True)),
                ('ldl_cholestrol', models.FloatField(null=True, blank=True)),
                ('triglycerides', models.FloatField(null=True, blank=True)),
                ('rbc', models.FloatField()),
                ('pus_cells', models.FloatField(null=True, blank=True)),
                ('epithelial_cells', models.CharField(max_length=5, null=True, blank=True)),
                ('estrone', models.FloatField(null=True, blank=True)),
                ('estradiol', models.FloatField(null=True, blank=True)),
                ('progesterone', models.FloatField(null=True, blank=True)),
                ('testosterone', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'test',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_doctor', models.BooleanField(default=False)),
                ('is_patient', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_profile',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('patient', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('test', models.ForeignKey(to='labmanagement.Test')),
            ],
            options={
                'db_table': 'user_test',
            },
            bases=(models.Model,),
        ),
    ]
