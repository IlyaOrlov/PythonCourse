# Generated by Django 3.0.8 on 2020-10-19 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coolapp', '0004_auto_20201019_2024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentary',
            old_name='film_id',
            new_name='film',
        ),
    ]