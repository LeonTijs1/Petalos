# Generated by Django 2.2.6 on 2019-10-18 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petalos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flor',
            old_name='stock',
            new_name='cantidad',
        ),
        migrations.RemoveField(
            model_name='flor',
            name='estado',
        ),
    ]
