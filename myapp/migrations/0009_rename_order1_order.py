# Generated by Django 4.0.5 on 2022-07-16 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_order1'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order1',
            new_name='Order',
        ),
    ]