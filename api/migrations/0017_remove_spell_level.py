# Generated by Django 3.2.18 on 2023-04-14 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_rename_level_int_spell_spell_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spell',
            name='level',
        ),
    ]
