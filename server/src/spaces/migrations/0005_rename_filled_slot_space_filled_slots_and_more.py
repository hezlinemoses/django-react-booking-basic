# Generated by Django 4.2 on 2023-04-30 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0004_slot_slot_id_alter_space_name_slot_unique_id_space'),
    ]

    operations = [
        migrations.RenameField(
            model_name='space',
            old_name='filled_slot',
            new_name='filled_slots',
        ),
        migrations.RenameField(
            model_name='space',
            old_name='max_slot',
            new_name='max_slots',
        ),
    ]
