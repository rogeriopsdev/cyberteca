# Generated by Django 4.1.2 on 2022-10-28 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=255)),
                ('chamada', models.CharField(max_length=255)),
                ('titulo', models.CharField(max_length=255)),
                ('ano', models.CharField(max_length=255)),
                ('data_cadastro', models.CharField(max_length=255)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='')),
                ('autoresid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cybertecaapp.autores')),
                ('categoriaid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cybertecaapp.categorias')),
            ],
        ),
    ]
