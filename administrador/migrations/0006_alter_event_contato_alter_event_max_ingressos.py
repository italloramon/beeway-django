# Generated by Django 4.1.7 on 2023-04-18 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0005_event_contato_event_max_ingressos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='contato',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='event',
            name='max_ingressos',
            field=models.PositiveSmallIntegerField(),
        ),
    ]