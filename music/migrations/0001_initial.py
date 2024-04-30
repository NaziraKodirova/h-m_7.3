# Generated by Django 5.0.4 on 2024-04-30 18:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Albom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('cover', models.URLField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='music.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cover', models.URLField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('albom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='music.albom')),
            ],
        ),
    ]
