# Generated by Django 3.0.3 on 2020-03-09 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrApp', '0004_auto_20200309_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedatabaseform',
            name='emergencyContact',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employeedatabaseform',
            name='empId',
            field=models.IntegerField(),
        ),
    ]
