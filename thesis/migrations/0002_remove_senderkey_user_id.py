# Generated by Django 3.1.6 on 2021-03-30 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='senderkey',
            name='user_id',
        ),
    ]
