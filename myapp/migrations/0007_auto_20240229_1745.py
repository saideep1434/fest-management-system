# Generated by Django 3.2.18 on 2024-02-29 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_volunteer'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='student_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='student_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.event'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='event_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.student'),
        ),
    ]