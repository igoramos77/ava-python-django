# Generated by Django 2.2.19 on 2021-04-13 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0012_auto_20210413_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='credito',
            field=models.IntegerField(default=30, verbose_name='Créditos'),
            preserve_default=False,
        ),
    ]