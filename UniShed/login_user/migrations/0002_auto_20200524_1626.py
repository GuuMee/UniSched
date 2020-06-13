# Generated by Django 3.0.5 on 2020-05-24 13:26

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('login_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='birth_date',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='middle_name',
            field=models.CharField(max_length=30, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Телефон'),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='login_user.Faculty')),
            ],
        ),
    ]