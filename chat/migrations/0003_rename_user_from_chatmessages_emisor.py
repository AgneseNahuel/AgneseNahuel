# Generated by Django 4.1 on 2022-12-20 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_chatmessages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatmessages',
            old_name='user_from',
            new_name='emisor',
        ),
    ]
