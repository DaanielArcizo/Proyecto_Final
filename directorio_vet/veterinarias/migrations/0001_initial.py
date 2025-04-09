# Generated by Django 5.1.7 on 2025-03-27 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Veterinaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('horario', models.CharField(max_length=255)),
                ('admite_emergencias', models.BooleanField(default=False)),
            ],
        ),
    ]
