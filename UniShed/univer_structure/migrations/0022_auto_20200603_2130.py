# Generated by Django 3.0.5 on 2020-06-03 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('univer_structure', '0021_auditorium_type_discipline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditorium',
            name='type_of_auditorium',
            field=models.CharField(choices=[('Аудитория', 'Аудитория'), ('Уч. Лаб.', 'Учебная Лабораторная'), ('Уч. класс', 'Учебный класс'), ('Комп. класс', 'Компьютерные класс'), ('Каф. а.', 'Аудитория кафедры')], default='Аудитория', max_length=30, verbose_name='Тип аудитории'),
        ),
    ]