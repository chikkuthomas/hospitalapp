# Generated by Django 3.2.5 on 2021-08-27 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='time_slot',
            field=models.TimeField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='status',
            field=models.CharField(choices=[('booked_slot', 'booked_slot'), ('cancelled_appoinment', 'cancelled_appoinment'), ('no_booking', 'no_booking'), ('appointed', 'appointed')], default='no_booking', max_length=40),
        ),
    ]
