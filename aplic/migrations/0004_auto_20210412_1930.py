# Generated by Django 2.2.19 on 2021-04-12 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0003_auto_20210412_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='periodo',
            field=models.CharField(choices=[('1', '1º'), ('2', '2º'), ('3', '3º'), ('4', '4º'), ('5', '5º'), ('6', '6º'), ('7', '7º'), ('8', '8º'), ('9', '9º'), ('10', '10º')], max_length=3, verbose_name='Período'),
        ),
    ]
