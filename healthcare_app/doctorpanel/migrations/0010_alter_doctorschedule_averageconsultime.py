# Generated by Django 4.0.4 on 2022-05-05 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorpanel', '0009_alter_doctorschedule_endtime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorschedule',
            name='averageconsultime',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
