# Generated by Django 4.1.2 on 2022-10-13 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='district',
            old_name='district',
            new_name='state',
        ),
    ]