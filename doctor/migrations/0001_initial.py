# Generated by Django 3.2.5 on 2021-08-16 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=120)),
                ('speciality', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='images')),
                ('specialist', models.CharField(max_length=120)),
                ('about', models.CharField(max_length=500)),
                ('start_time', models.PositiveIntegerField(default=10)),
                ('end_time', models.PositiveIntegerField(default=10)),
                ('availability', models.CharField(max_length=120)),
            ],
        ),
    ]
