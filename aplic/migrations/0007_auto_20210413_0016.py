# Generated by Django 2.2.19 on 2021-04-13 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0006_auto_20210412_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turma',
            name='disciplina',
        ),
        migrations.AddField(
            model_name='turma',
            name='disciplina',
            field=models.ManyToManyField(to='aplic.Disciplina'),
        ),
    ]
