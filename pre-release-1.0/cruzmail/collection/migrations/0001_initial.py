# Generated by Django 2.0.6 on 2019-02-17 10:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mailstops_master',
            fields=[
                ('mailstop', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('ms_status', models.CharField(choices=[('0', 'active'), ('1', 'inactive')], default='0', max_length=1)),
                ('ms_route', models.CharField(choices=[('w', 'West'), ('c', 'central'), ('e', 'east')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='packages_master',
            fields=[
                ('pkg_tracking', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('pkg_status', models.CharField(choices=[('r', 'recieved'), ('d', 'delivered')], max_length=1)),
                ('pkg_sign', models.CharField(choices=[('y', 'yes'), ('n', 'no')], default='n', max_length=1)),
                ('pkg_email', models.CharField(choices=[('y', 'yes'), ('n', 'no')], default='y', max_length=1)),
                ('pkg_weight', models.CharField(choices=[('s', '1 to 5'), ('m', '6 to 15'), ('l', 'over 16')], max_length=1)),
                ('pkg_date_rec', models.DateField(default=datetime.date.today)),
                ('pkg_date_del', models.DateField(default=datetime.date.today)),
                ('pkg_remarks', models.CharField(max_length=144)),
            ],
        ),
        migrations.CreateModel(
            name='people_master',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=20)),
                ('mailstop', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, to='collection.mailstops_master')),
            ],
        ),
        migrations.AddField(
            model_name='packages_master',
            name='mailstop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='collection.mailstops_master'),
        ),
        migrations.AddField(
            model_name='packages_master',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='collection.people_master'),
        ),
    ]
