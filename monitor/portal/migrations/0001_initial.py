# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-01 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mn_alert2action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_name', models.CharField(max_length=30)),
                ('alert_actions', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='mn_Ansible_action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_name', models.CharField(max_length=30)),
                ('action_desc', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='mn_Ansible_git_para',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('git_url', models.CharField(max_length=300)),
                ('git_pubkey', models.CharField(max_length=300)),
                ('git_prvkey', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='mn_DeviceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='mn_Enterprise_wechat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corp_id', models.CharField(max_length=100)),
                ('app_secret', models.CharField(max_length=100)),
                ('app_id', models.IntegerField(default=0)),
                ('user_ids', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='mn_NetDevices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_type', models.CharField(max_length=30)),
                ('device_ip', models.CharField(max_length=30)),
                ('device_mac', models.CharField(max_length=30)),
                ('memo', models.CharField(default='please add some description here', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='mn_OSTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ostype', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='mn_routine_crob_job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_name', models.CharField(max_length=30)),
                ('target_name', models.CharField(max_length=100)),
                ('cron_paras', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='mn_routine_op_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_name', models.CharField(max_length=30)),
                ('group_name', models.CharField(max_length=100)),
                ('target_name', models.CharField(max_length=100)),
                ('invoke_times', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='mn_ServerGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=30)),
                ('listen_port', models.IntegerField(default=9100)),
            ],
        ),
        migrations.CreateModel(
            name='mn_Servers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sip', models.CharField(max_length=30)),
                ('smac', models.CharField(max_length=30)),
                ('sostype', models.CharField(max_length=30)),
                ('smodel', models.CharField(max_length=100)),
                ('sgroup1', models.CharField(max_length=50)),
                ('sgroup2', models.CharField(max_length=50)),
                ('sgroup3', models.CharField(max_length=50)),
                ('sgroup4', models.CharField(max_length=50)),
                ('sadmin', models.CharField(max_length=30)),
                ('spasswd', models.CharField(max_length=30)),
                ('memo', models.CharField(default='please add some description here', max_length=300)),
            ],
        ),
    ]