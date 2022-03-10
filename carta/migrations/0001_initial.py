# Generated by Django 3.2.8 on 2022-03-07 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventario', '0003_remove_inventario_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_platillo', models.CharField(max_length=200, unique=True)),
                ('descripcion', models.TextField(blank=True, max_length=500)),
                ('precio', models.IntegerField()),
                ('images', models.ImageField(upload_to='photos/menu')),
                ('stock', models.IntegerField()),
                ('disponible', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.inventario')),
            ],
        ),
    ]