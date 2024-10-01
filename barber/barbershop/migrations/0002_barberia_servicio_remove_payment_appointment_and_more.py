# Generated by Django 5.1.1 on 2024-09-04 13:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbershop', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Barberia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(max_length=20)),
                ('horario_apertura', models.TimeField()),
                ('horario_cierre', models.TimeField()),
                ('descripcion', models.TextField()),
                ('imagen_logo', models.ImageField(blank=True, null=True, upload_to='barberias_logos/')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('duracion_estimada', models.DurationField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.RemoveField(
            model_name='payment',
            name='appointment',
        ),
        migrations.RemoveField(
            model_name='barber',
            name='barbershop',
        ),
        migrations.RemoveField(
            model_name='barber',
            name='user',
        ),
        migrations.RemoveField(
            model_name='haircutphoto',
            name='barber',
        ),
        migrations.RemoveField(
            model_name='review',
            name='barber',
        ),
        migrations.RemoveField(
            model_name='haircutphoto',
            name='haircut_style',
        ),
        migrations.RemoveField(
            model_name='review',
            name='customer',
        ),
        migrations.CreateModel(
            name='BarberFace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_rostro', models.ImageField(upload_to='barberface/')),
                ('fecha_escaneo', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Barbero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificado_profesional', models.FileField(blank=True, null=True, upload_to='certificados/')),
                ('anos_experiencia', models.IntegerField()),
                ('especialidad', models.CharField(max_length=100)),
                ('disponibilidad', models.TextField()),
                ('barberia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbershop.barberia')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CatalogoCortes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_estilo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='catalogo_cortes/')),
                ('barbero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbershop.barbero')),
            ],
        ),
        migrations.CreateModel(
            name='Contabilidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('ingresos_totales', models.DecimalField(decimal_places=2, max_digits=10)),
                ('gastos_totales', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ganancia_neta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('barberia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbershop.barberia')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleContabilidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=8)),
                ('tipo', models.CharField(choices=[('ingreso', 'Ingreso'), ('gasto', 'Gasto')], max_length=10)),
                ('concepto', models.CharField(max_length=200)),
                ('barbero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='barbershop.barbero')),
                ('registro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbershop.contabilidad')),
            ],
        ),
        migrations.CreateModel(
            name='EstilosSugeridos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentaje_coincidencia', models.FloatField()),
                ('barberface', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbershop.barberface')),
                ('corte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbershop.catalogocortes')),
            ],
        ),
        migrations.CreateModel(
            name='Promociones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('descuento', models.DecimalField(decimal_places=2, max_digits=5)),
                ('barberia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbershop.barberia')),
            ],
        ),
        migrations.CreateModel(
            name='RankingBarberos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntuacion_promedio', models.FloatField()),
                ('total_resenas', models.IntegerField()),
                ('posicion_ranking', models.IntegerField()),
                ('barbero', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='barbershop.barbero')),
            ],
        ),
        migrations.CreateModel(
            name='Resena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('comentario', models.TextField()),
                ('fecha_resena', models.DateTimeField(auto_now_add=True)),
                ('barbero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbershop.barbero')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=8)),
                ('metodo_pago', models.CharField(choices=[('efectivo', 'Efectivo'), ('nequi', 'Nequi')], max_length=20)),
                ('fecha_pago', models.DateTimeField(auto_now_add=True)),
                ('estado_pago', models.BooleanField(default=False)),
                ('barbero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbershop.barbero')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbershop.servicio')),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
                ('direccion_formatted', models.CharField(max_length=255)),
                ('barberia', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='barbershop.barberia')),
            ],
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='Barbershop',
        ),
        migrations.DeleteModel(
            name='Barber',
        ),
        migrations.DeleteModel(
            name='HaircutPhoto',
        ),
        migrations.DeleteModel(
            name='HaircutStyle',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]