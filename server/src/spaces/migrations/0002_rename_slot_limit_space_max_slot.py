# Generated by Django 4.2 on 2023-04-29 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='space',
            old_name='slot_limit',
            new_name='max_slot',
        ),
    ]
