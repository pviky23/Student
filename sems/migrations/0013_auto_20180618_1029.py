# Generated by Django 2.0.4 on 2018-06-18 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sems', '0012_remove_provimet_times'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provimet',
            name='course',
        ),
        migrations.AddField(
            model_name='provimet',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sems.Course'),
        ),
    ]
