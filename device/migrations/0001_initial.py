# Generated by Django 3.1.6 on 2021-02-03 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('status', models.CharField(default='', max_length=255)),
                ('chassis_type', models.CharField(default='', max_length=255)),
                ('service_type', models.CharField(default='', max_length=255)),
                ('device_type', models.CharField(default='', max_length=255)),
                ('toposite_name', models.CharField(default='', max_length=255)),
                ('site_name', models.CharField(default='', max_length=255)),
                ('ico01', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'devices',
            },
        ),
    ]
