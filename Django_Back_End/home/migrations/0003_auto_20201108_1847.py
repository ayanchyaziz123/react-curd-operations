# Generated by Django 3.0.7 on 2020-11-08 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20201108_1836'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='userId',
            new_name='id',
        ),
    ]