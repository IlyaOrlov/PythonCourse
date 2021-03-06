# Generated by Django 3.0.8 on 2020-10-19 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coolapp', '0002_film_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_id', models.IntegerField()),
                ('author', models.CharField(max_length=100)),
                ('comm', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='date of creation')),
            ],
        ),
    ]
