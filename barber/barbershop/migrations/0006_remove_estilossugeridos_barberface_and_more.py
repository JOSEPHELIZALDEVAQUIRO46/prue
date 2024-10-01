# Generated by Django 5.1.1 on 2024-09-16 20:45

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbershop', '0005_alter_profile_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estilossugeridos',
            name='barberface',
        ),
        migrations.RemoveField(
            model_name='estilossugeridos',
            name='corte',
        ),
        migrations.RemoveField(
            model_name='pago',
            name='barbero',
        ),
        migrations.RemoveField(
            model_name='pago',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='pago',
            name='servicio',
        ),
        migrations.RemoveField(
            model_name='rankingbarberos',
            name='barbero',
        ),
        migrations.RemoveField(
            model_name='resena',
            name='barbero',
        ),
        migrations.RemoveField(
            model_name='resena',
            name='cliente',
        ),
        migrations.RenameField(
            model_name='contabilidad',
            old_name='ganancia_neta',
            new_name='gastos',
        ),
        migrations.RenameField(
            model_name='contabilidad',
            old_name='gastos_totales',
            new_name='ingresos',
        ),
        migrations.RemoveField(
            model_name='contabilidad',
            name='barberia',
        ),
        migrations.RemoveField(
            model_name='contabilidad',
            name='ingresos_totales',
        ),
        migrations.AlterField(
            model_name='contabilidad',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='BarberFace',
        ),
        migrations.DeleteModel(
            name='EstilosSugeridos',
        ),
        migrations.DeleteModel(
            name='Pago',
        ),
        migrations.DeleteModel(
            name='RankingBarberos',
        ),
        migrations.DeleteModel(
            name='Resena',
        ),
    ]