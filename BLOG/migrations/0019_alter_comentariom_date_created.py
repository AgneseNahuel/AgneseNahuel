# Generated by Django 4.1 on 2022-12-20 22:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BLOG', '0018_alter_comentariom_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentariom',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 20, 22, 55, 54, 428180, tzinfo=datetime.timezone.utc)),
        ),
    ]
