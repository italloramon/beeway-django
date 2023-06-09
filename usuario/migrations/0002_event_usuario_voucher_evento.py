# Generated by Django 4.1.7 on 2023-05-04 01:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='voucher',
            name='evento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='usuario.event'),
            preserve_default=False,
        ),
    ]
