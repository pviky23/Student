# Generated by Django 2.0.4 on 2018-06-22 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sems', '0017_auto_20180621_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='provimet',
            name='afati',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sems.afatet_provimeve'),
        ),
    ]