# Generated by Django 4.1 on 2022-12-16 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BLOG', '0003_alter_comentariom_subtitulo_alter_comentariom_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentariom',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='BlogImagen'),
        ),
    ]
