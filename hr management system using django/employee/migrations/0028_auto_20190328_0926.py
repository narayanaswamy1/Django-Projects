# Generated by Django 2.1.7 on 2019-03-28 09:26

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0027_employee_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employeetype',
            field=models.CharField(choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time'), ('Contract', 'Contract'), ('Intern', 'Intern')], default='Full-Time', max_length=15, null=True, verbose_name='Employee Type'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='tel',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default='+233240000000', help_text='Enter number with Country Code Eg. +233240000000', max_length=128, null=True, verbose_name='Spouse Phone Number (Example +233240000000)'),
        ),
    ]
