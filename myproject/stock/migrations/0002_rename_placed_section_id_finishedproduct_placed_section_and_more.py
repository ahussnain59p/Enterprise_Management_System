# Generated by Django 5.0.7 on 2024-07-28 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='finishedproduct',
            old_name='placed_section_id',
            new_name='placed_section',
        ),
        migrations.RenameField(
            model_name='rawmaterial',
            old_name='placed_section_id',
            new_name='placed_section',
        ),
    ]
