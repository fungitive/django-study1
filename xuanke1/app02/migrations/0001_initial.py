# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-19 07:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('班级', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('姓名', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=20, verbose_name='年龄')),
                ('gender', models.BooleanField()),
                ('birth', models.DateTimeField(auto_now_add=True, verbose_name='选课时间')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app02.Grade')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('老师姓名', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='grade',
            name='teacher',
            field=models.ManyToManyField(to='app02.Teacher'),
        ),
    ]
