# Generated by Django 2.2.19 on 2021-03-26 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0002_auto_20210326_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arquivo',
            name='nome_do_arquivo',
            field=models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name='Nome do Arquivo'),
        ),
    ]
