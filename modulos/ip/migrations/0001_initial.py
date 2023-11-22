# Generated by Django 4.2.4 on 2023-08-20 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'País',
                'verbose_name_plural': 'Países',
            },
        ),
        migrations.CreateModel(
            name='DireccionIP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion_IP', models.GenericIPAddressField(unique=True, verbose_name='Dirección IP')),
                ('pais', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ip.pais')),
            ],
            options={
                'verbose_name': 'Dirección IP',
                'verbose_name_plural': 'Direcciones IP',
            },
        ),
    ]