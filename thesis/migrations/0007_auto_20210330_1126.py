# Generated by Django 3.1.6 on 2021-03-30 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesis', '0006_uploaddata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploaddata',
            old_name='image',
            new_name='datafile',
        ),
    ]
