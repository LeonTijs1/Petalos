# Generated by Django 2.2.6 on 2019-10-08 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flor',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('imagen', models.ImageField(null=True, upload_to='flores')),
                ('stock', models.IntegerField()),
                ('valor', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('estado', models.BooleanField()),
            ],
        ),
    ]