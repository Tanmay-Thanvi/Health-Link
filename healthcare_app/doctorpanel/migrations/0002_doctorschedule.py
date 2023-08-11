# Generated by Django 4.0.4 on 2022-05-05 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctorpanel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctorschedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Daysavail', models.CharField(max_length=50)),
                ('Timeavail', models.TimeField()),
                ('Doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='doctorpanel.doctor')),
            ],
        ),
    ]
