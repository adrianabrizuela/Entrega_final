# Generated by Django 5.0.3 on 2024-05-01 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='imagen',
        ),
    ]