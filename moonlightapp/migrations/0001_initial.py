# Generated by Django 2.0.4 on 2018-04-22 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='PodDevices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_url', models.CharField(max_length=500)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moonlightapp.Device')),
                ('pod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moonlightapp.Pod')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='pod',
            name='devices',
            field=models.ManyToManyField(through='moonlightapp.PodDevices', to='moonlightapp.Device'),
        ),
    ]
