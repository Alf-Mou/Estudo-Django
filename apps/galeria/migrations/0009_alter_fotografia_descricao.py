# Generated by Django 5.0.4 on 2024-07-29 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0008_alter_fotografia_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='descricao',
            field=models.TextField(),
        ),
    ]
