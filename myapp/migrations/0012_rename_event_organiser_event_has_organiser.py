# Generated by Django 3.2.18 on 2024-03-02 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_event_organiser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='event_organiser',
            new_name='Event_has_organiser',
        ),
    ]