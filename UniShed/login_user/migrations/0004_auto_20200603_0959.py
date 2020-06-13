# Generated by Django 3.0.5 on 2020-06-03 06:59

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('login_user', '0003_auto_20200529_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True, verbose_name='Телефон'),
        ),
    ]