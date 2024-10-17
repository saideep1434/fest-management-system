# Generated by Django 3.2.18 on 2024-02-28 19:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_eventregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('vacancy', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hall2',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('vacancy', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Accomadation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_par', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.externalparticipant')),
                ('name_hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.hall')),
            ],
        ),
    ]
