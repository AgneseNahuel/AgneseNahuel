# Generated by Django 4.1 on 2022-12-17 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BLOG', '0013_alter_comentariom_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentariom',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/imagenBlog'),
        ),
    ]
