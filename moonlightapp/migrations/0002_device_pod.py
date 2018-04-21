# Generated by Django 2.0.4 on 2018-04-21 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moonlightapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('type', models.CharField(choices=[('ROUTER', 'Router'), ('SWITCH', 'Switch'), ('ACCESS_POINT', 'Access Point'), ('TS', 'Terminal Server')], max_length=10)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Pod',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('devices', models.ManyToManyField(to='moonlightapp.Device')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]