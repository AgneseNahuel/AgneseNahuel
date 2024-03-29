# Generated by Django 4.1 on 2022-12-16 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BLOG', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
        migrations.CreateModel(
            name='comentarioM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo', models.TextField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='avatares')),
                ('titulo', models.TextField()),
                ('subtitulo', models.TextField()),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
