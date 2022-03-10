# Generated by Django 3.2.8 on 2022-03-08 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proveedor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_producto', models.CharField(max_length=200, unique=True)),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('estado', models.BooleanField(default=False)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedor.proveedor')),
            ],
        ),
    ]